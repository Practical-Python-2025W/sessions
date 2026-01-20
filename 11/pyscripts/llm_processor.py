"""Helper class to call a local Ollama model for text processing."""
import json
from typing import Optional
import ollama


class LLMProcessor:
	"""Call a local Ollama model on plain text."""

	def __init__(
		self,
		model: str = "llama3.2",
	) -> None:
		self.model = model

	def generate_text(self, text: str, instructions: Optional[str] = None) -> str:
		"""Return a free-form answer for the given text."""
		if instructions:
			user_content = f"{instructions}\n\nText:\n{text}"
		else:
			user_content = f"Text:\n{text}"
		return self._chat(user_content=user_content, system_prompt=None)

	def generate_structured(self, text: str, schema, instructions: str) -> object:
		"""Return a Pydantic model instance built from the text.

		``schema`` is expected to be a ``pydantic.BaseModel`` subclass.
		"""
		# Build JSON schema description for the system prompt.
		if hasattr(schema, "model_json_schema"):
			schema_json = json.dumps(schema.model_json_schema(), indent=2)
		else:
			schema_json = json.dumps(schema.schema(), indent=2)

		system_prompt = (
			"You are a JSON API. Respond only with valid JSON "
			"that matches this schema:\n\n"
			f"{schema_json}"
		)

		user_content = f"{instructions}\n\nText:\n{text}"

		raw = self._chat(user_content=user_content, system_prompt=system_prompt)
		data = _parse_json(raw)

		if hasattr(schema, "model_validate"):
			return schema.model_validate(data)
		if hasattr(schema, "parse_obj"):
			return schema.parse_obj(data)

		return schema(**data)

	def _chat(self, user_content: str, system_prompt: Optional[str]) -> str:
		"""Send a single chat request to Ollama and return the reply text."""

		messages = []
		if system_prompt:
			messages.append({"role": "system", "content": system_prompt})
		messages.append({"role": "user", "content": user_content})

		resp = ollama.chat(model=self.model, messages=messages)
		try:
			return resp["message"]["content"]
		except Exception as exc:
			raise RuntimeError(f"Unexpected Ollama response: {resp!r}") from exc


def _parse_json(raw: str):
	"""Parse JSON from a model answer, handling simple markdown fences."""

	raw = raw.strip()
	try:
		return json.loads(raw)
	except json.JSONDecodeError:
		pass

	# Handle ```json ... ``` style output.
	if raw.startswith("```"):
		lines = raw.splitlines()
		if len(lines) >= 2:
			raw = "\n".join(lines[1:])
		if raw.endswith("```"):
			raw = raw.rsplit("```", 1)[0]
		raw = raw.strip()
		return json.loads(raw)

	raise json.JSONDecodeError("Could not parse JSON", raw, 0)


def process_with_ollama(text: str, instructions: Optional[str] = None, model: str = "llama3.2") -> str:
	"""Shortcut for ``LLMProcessor().generate_text(...)``."""

	return LLMProcessor(model=model).generate_text(text, instructions=instructions)


def process_structured_with_ollama(text: str, schema, instructions: str, model: str = "llama3.2"):
	"""Shortcut for ``LLMProcessor().generate_structured(...)``."""

	return LLMProcessor(model=model).generate_structured(text, schema, instructions)