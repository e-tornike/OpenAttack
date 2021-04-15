from .default import DefaultAttackEval
from ..classifier import Classifier
from ..attacker import Attacker


class ChineseAttackEval(DefaultAttackEval):
    """
    ChineseAttackEval is the implementation of AttackEval for chinese datasets and models.
    """

    def __init__(self, attacker, classifier, **kwargs):
        """
        :param Attacker attacker: The attacker you use.
        :param Classifier classifier: The classifier you want to attack.
        :param kwargs: Other parameters, see :py:class:`.DefaultAttackEval` for detail.
        """
        if kwargs["processor"] is None:
            from ..text_processors import ChineseTextProcessor
            kwargs["processor"] = ChineseTextProcessor()
        if kwargs["language_model"] is None:
            from ..metric import GPT2LMCH
            kwargs["language_model"] = GPT2LMCH()
        if kwargs["language_tool"] is None:
            from ..metric import ChineseLanguageTool
            kwargs["language_tool"] = ChineseLanguageTool()
        super().__init__(attacker, classifier, **kwargs)

        self.__attacker = self.attacker
        self.__classifier = self.classifier
