from .base import MetricSelector
class Fluency(MetricSelector):
    """
    :English: :py:class:`.GPT2LM`
    :Chinese: :py:class:`.GPT2LMChinese`
    """

    def _select(self, lang):
        if lang.name in ["english", "german"]:
            from ..algorithms.gptlm import GPT2LM
            return GPT2LM(lang=lang.name)
        if lang.name == "chinese":
            from ..algorithms.gptlm import GPT2LMChinese
            return GPT2LMChinese()