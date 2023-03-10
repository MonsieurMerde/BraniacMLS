from django.db import migrations


def forwards_func(apps, schema_editor):
    Lesson = apps.get_model("mainapp", "Lesson")
    Courses = apps.get_model("mainapp", "Courses")

    Lesson.objects.create(
        course=Courses.objects.get(id="1"),
        num="1",
        title="Lesson 1",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="1"),
        num="2",
        title="Lesson 2",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="1"),
        num="3",
        title="Lesson 3",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="1"),
        num="4",
        title="Lesson 4",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="1"),
        num="5",
        title="Lesson 5",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="1"),
        num="6",
        title="Lesson 6",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="1"),
        num="7",
        title="Lesson 7",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="1"),
        num="8",
        title="Lesson 8",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="2"),
        num="1",
        title="Lesson 1",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="2"),
        num="2",
        title="Lesson 2",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="2"),
        num="3",
        title="Lesson 3",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="2"),
        num="4",
        title="Lesson 4",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="2"),
        num="5",
        title="Lesson 5",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="2"),
        num="6",
        title="Lesson 6",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="2"),
        num="7",
        title="Lesson 7",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="2"),
        num="8",
        title="Lesson 8",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="3"),
        num="1",
        title="Lesson 1",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="3"),
        num="2",
        title="Lesson 2",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="3"),
        num="3",
        title="Lesson 3",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="3"),
        num="4",
        title="Lesson 4",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="3"),
        num="5",
        title="Lesson 5",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="3"),
        num="6",
        title="Lesson 6",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="3"),
        num="7",
        title="Lesson 7",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="3"),
        num="8",
        title="Lesson 8",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="4"),
        num="1",
        title="Lesson 1",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="4"),
        num="2",
        title="Lesson 2",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="4"),
        num="3",
        title="Lesson 3",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="4"),
        num="4",
        title="Lesson 4",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="4"),
        num="5",
        title="Lesson 5",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="4"),
        num="6",
        title="Lesson 6",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="4"),
        num="7",
        title="Lesson 7",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="4"),
        num="8",
        title="Lesson 8",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="5"),
        num="1",
        title="Lesson 1",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="5"),
        num="2",
        title="Lesson 2",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="5"),
        num="3",
        title="Lesson 3",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="5"),
        num="4",
        title="Lesson 4",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="5"),
        num="5",
        title="Lesson 5",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="5"),
        num="6",
        title="Lesson 6",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="5"),
        num="7",
        title="Lesson 7",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="5"),
        num="8",
        title="Lesson 8",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="6"),
        num="1",
        title="Lesson 1",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="6"),
        num="2",
        title="Lesson 2",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="6"),
        num="3",
        title="Lesson 3",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="6"),
        num="4",
        title="Lesson 4",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="6"),
        num="5",
        title="Lesson 5",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="6"),
        num="6",
        title="Lesson 6",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="6"),
        num="7",
        title="Lesson 7",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="6"),
        num="8",
        title="Lesson 8",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="7"),
        num="1",
        title="Lesson 1",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="7"),
        num="2",
        title="Lesson 2",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="7"),
        num="3",
        title="Lesson 3",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="7"),
        num="4",
        title="Lesson 4",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="7"),
        num="5",
        title="Lesson 5",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="7"),
        num="6",
        title="Lesson 6",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="7"),
        num="7",
        title="Lesson 7",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="7"),
        num="8",
        title="Lesson 8",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="8"),
        num="1",
        title="Lesson 1",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="8"),
        num="2",
        title="Lesson 2",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="8"),
        num="3",
        title="Lesson 3",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="8"),
        num="4",
        title="Lesson 4",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="8"),
        num="5",
        title="Lesson 5",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="8"),
        num="6",
        title="Lesson 6",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="8"),
        num="7",
        title="Lesson 7",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )
    Lesson.objects.create(
        course=Courses.objects.get(id="8"),
        num="8",
        title="Lesson 8",
        description="Описание урока",
        description_as_markdown="False",
        created="2021-07-11T12:53:26.832Z",
        updated="2021-07-11T12:53:26.833Z",
    )


def reverse_func(apps, schema_editor):
    Lesson = apps.get_model("mainapp", "Lesson")
    Lesson.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0003_data_courses"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
