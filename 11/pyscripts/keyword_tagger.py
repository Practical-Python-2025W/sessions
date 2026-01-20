"""Two-step helper for keyword-based tagging with a local Ollama model.

Usage::

    from keyword_tagger import tag_with_keywords

    tagged = tag_with_keywords(text, model="llama3.2")

This will first ask the model for a list of keywords in *text*, then start
a fresh chat that takes those keywords and returns the same text back with
those keywords (or very close variants) tagged in-place.
"""

from typing import List, Optional

from ollama_chat import chat, OllamaConfig


def _extract_keywords(
    text: str,
    config: OllamaConfig,
) -> List[str]:
    """Ask the model for a plain, comma-separated keyword list.

    We keep the prompt strict so it's easy to split the result.
    """

    system_prompt = (
        "You are a keyword extractor. Given some text, return a small "
        "list of important keywords, separated by commas in a single "
        "line. Do not add explanations, numbering, or extra text."
    )

    user_instructions = f"Text:\n{text}"

    raw = chat(
        config=config,
        user_instructions=user_instructions,
        system_prompt=system_prompt,
    )

    # Very simple parsing: split on commas, strip whitespace, drop empties.
    keywords = [kw.strip() for kw in raw.replace("\n", " ").split(",")]
    return [kw for kw in keywords if kw]

def tag_with_keywords(
    text: str,
    extract_config: Optional[OllamaConfig] = None,
    tag_config: Optional[OllamaConfig] = None,
) -> str:
    """Tag occurrences of model-extracted keywords in *text*.

    This is a two-step process:

     1. Call the model once to get a comma-separated list of keywords
         (using ``extract_config``).
     2. Start a new chat and ask the model to return the original text,
         but with those keywords highlighted in a simple XML-like form
         (using ``tag_config``)::

           <keyword>Python</keyword>

    The function returns whatever the second call outputs (ideally the
    tagged text).

    If a config is ``None``, a default ``OllamaConfig()`` is used.
    If individual fields on a config are left as ``None``, Ollama's
    own defaults apply for those options.
    """

    base_config = OllamaConfig()
    extract_config = extract_config or base_config
    tag_config = tag_config or extract_config

    keywords = _extract_keywords(
        text=text,
        config=extract_config,
    )

    keyword_list = ", ".join(keywords) if keywords else ""

    system_prompt = (
        "You are a tagger. You will receive some text and a list of "
        "keywords. Return the SAME text, but wrap each occurrence of "
        "one to three words closely related to each keyword "
        "in the tag <marked>...</marked>.\n\n"
        "Important: always use exactly the tag name 'marked' "
        "(i.e. <marked> and </marked>). Do not use the keyword itself "
        "as the tag name, and do not add any explanations or extra text. "
        "Only output the tagged text."
    )

    user_instructions = (
        "Here is the text and the keywords you should tag.\n\n"
        f"Keywords:\n{keyword_list}\n"
        f"Text:\n{text}\n\n"
    )

    return chat(
        config=tag_config,
        user_instructions=user_instructions,
        system_prompt=system_prompt,
    )


def test() -> None:
    """Small manual test for ``tag_with_keywords``."""

    sample_text = (
        "Python is a popular programming language used for data science, "
        "web development, and automation in many companies and research labs."
        "Python has gained widespread use in the machine learning community. "
        "It is widely taught as an introductory programming language. Since 2003, "
        "Python has consistently ranked in the top ten of the most popular programming "
        "languages in the TIOBE Programming Community Index, which ranks based on searches in 24 platforms."
    )
    model = "ALIENTELLIGENCE/structureddataextraction:latest"

    print("Using model:", model)
    print("Original text:\n", sample_text, "\n", sep="")

    config = OllamaConfig(model=model, temperature=0.1)
    tagged = tag_with_keywords(sample_text, extract_config=config, tag_config=config)

    print("Tagged text:\n", tagged)


if __name__ == "__main__":
    test()
