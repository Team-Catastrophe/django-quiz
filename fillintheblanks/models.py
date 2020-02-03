from django.db import models

# Create your models here.
from quiz.models import Question

ANSWER_ORDER_OPTIONS = (
    ('content', 'Content'),
    ('none', 'None'),
    # ('random', 'Random')
)


class FillQuestion(Question):
    fill        = models.BooleanField(default=True)
    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ANSWER_ORDER_OPTIONS,
        help_text="The order in which multichoice \
                    answer options are displayed \
                    to the user",
        verbose_name="Answer Order")

    def check_if_correct(self, guess):
        answer = FillAnswer.objects.get(id=guess)

        if answer.correct is True:
            return True
        else:
            return False
    
    def order_answers(self, queryset):
        if self.answer_order == 'content':
            return queryset.order_by('content')
        # if self.answer_order == 'random':
        #     return queryset.order_by('Random')
        if self.answer_order == 'none':
            return queryset.order_by('None')

    def get_answers(self):
        return self.order_answers(FillAnswer.objects.filter(question=self))

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in self.order_answers(FillAnswer.objects.filter(question=self))]

    def answer_choice_to_string(self, guess):
        return Answer.objects.get(id=guess).content

    def get_fillanswer(self):
        answer = FillAnswer.objects.get(question=self)
        return answer.content

    class Meta:
        verbose_name = "Fill in the blank Question"
        verbose_name_plural = "Fill in the blank Question"


class FillAnswer(models.Model):
    question = models.ForeignKey(FillQuestion, verbose_name='Question', on_delete=models.CASCADE)
    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text="Fill in the blanks answer",
                               verbose_name="Content")
    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"





