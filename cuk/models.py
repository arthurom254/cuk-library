from django.db import models
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.
YR_CHOISE = (("1", 1), ("2", 2), ("3", 3), ("4", 4),)
SEM_CHOISE = (("1", 1), ("2", 2),)
TYPE_CHOISE = (
    ("Main Exam", "Main Exam"),
    ("Special Exam", "Special Exam"),
    ("Supplimentary Exam", "Supplimentary Exam"),
)


class School(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(max_length=500)
    abbr = models.CharField(max_length=30, null=True)
    schools = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Unit(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    course = ChainedManyToManyField(
        Course,
        horizontal=True,
        verbose_name="Course",
        chained_field="school",
        chained_model_field="schools"
    )
    name = models.CharField(max_length=500)
    year = models.CharField(max_length=5, choices=YR_CHOISE, default=4)
    def __str__(self):
        return f"{self.name}"


class Paper(models.Model):
    sem = models.CharField(max_length=5, choices=SEM_CHOISE, default=1)
    examyear = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOISE, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    courses = ChainedForeignKey(
        Course,
        verbose_name="courses",
        chained_field="school",
        chained_model_field="schools",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    units = ChainedForeignKey(
        Unit,
        verbose_name="unit",
        chained_field="courses",
        chained_model_field="course",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    questions = RichTextUploadingField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('study',args=[self.units,self.id,])

    class Meta:
        ordering=['examyear']
    def __str__(self):
        return f"Sem {self.sem} {self.type} {self.examyear} {self.units}"


#print(unit.course.first().abbr)