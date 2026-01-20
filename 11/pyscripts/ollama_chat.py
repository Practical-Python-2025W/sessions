import ollama
from dataclasses import dataclass
from typing import Optional


@dataclass
class OllamaConfig:
    """Configuration for a single Ollama call.

    All fields are optional except ``model``; if you leave a sampling
    parameter as ``None``, Ollama's built-in default for that option is
    used.
    """

    model: str = "llama3.2"
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    num_predict: Optional[int] = None


def chat(
    config: OllamaConfig,
    user_instructions: str,
    system_prompt: str,
) -> str:
    """Small wrapper around ``ollama.chat`` using :class:`OllamaConfig`.

    The ``config`` object controls model name and all optional sampling
    parameters. Any field left as ``None`` lets Ollama fall back to its
    own default for that option.

    Parameters
    ----------
    config:
        Instance of :class:`OllamaConfig` with model name and optional
        sampling settings like ``temperature``, ``top_p``, ``top_k``,
        and ``num_predict``.
    """

    options = {}
    if config.temperature is not None:
        options["temperature"] = config.temperature
    if config.top_p is not None:
        options["top_p"] = config.top_p
    if config.top_k is not None:
        options["top_k"] = config.top_k
    if config.num_predict is not None:
        options["num_predict"] = config.num_predict

    resp = ollama.chat(
        model=config.model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_instructions},
        ],
        options=options or None,
    )

    try:
        return resp["message"]["content"]
    except Exception as exc:  # pragma: no cover - defensive
        raise RuntimeError(f"Unexpected Ollama response: {resp!r}") from exc

if __name__ == "__main__":
    sample_text = (
        "Python is a popular programming language used for data science, "
        "web development, and automation in many companies and research labs."
        "Python has gained widespread use in the machine learning community. "
        "It is widely taught as an introductory programming language. Since 2003, "
        "Python has consistently ranked in the top ten of the most popular programming "
        "languages in the TIOBE Programming Community Index, which ranks based on searches in 24 platforms."
    )
    system_prompt = (
        "You are a research assistant. Highlight important word groups (max. length 4 words) "
        "in the input text. Place each important word group in a <mark></mark> tag. Return"
        "only the text with the marked word groups; do not add any explanations or extra text."
        "Return the full text even if no word groups were found."
    )
    user_instructions = (
        f"Text:\n{sample_text}\n\n"
    )

    config = OllamaConfig(
        model="llama3.2:latest",
        temperature=0.1,
        top_p=0.9,
        num_predict=5000,
    )

    tagged_text = chat(
        config=config,
        user_instructions=user_instructions,
        system_prompt=system_prompt,
    )

    print("Tagged text:\n", tagged_text, sep="")