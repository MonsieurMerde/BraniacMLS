from django.db import migrations


def forwards_func(apps, schema_editor):
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    Courses = apps.get_model("mainapp", "Courses")

    CourseTeachers.objects.create(
        name_first="Альфред",
        name_second="Нуцубидзе",
        day_birth="1990-07-10",
    )
    CourseTeachers.objects.create(
        name_first="Роман",
        name_second="Доржинов",
        day_birth="1988-02-04",
    )
    CourseTeachers.objects.create(
        name_first="Ярослав",
        name_second="Конягин",
        day_birth="1981-12-08",
    )
    CourseTeachers.objects.create(
        name_first="Автандил",
        name_second="Наварский",
        day_birth="1983-05-16",
    )
    CourseTeachers.objects.create(
        name_first="Роза",
        name_second="Уланова",
        day_birth="1986-05-09",
    )
    CourseTeachers.objects.create(
        name_first="Бронислава",
        name_second="Алиева",
        day_birth="1971-01-07",
    )
    CourseTeachers.objects.create(
        name_first="Диана",
        name_second="Попова",
        day_birth="1990-08-25",
    )

    courses = [
        [Courses.objects.get(id="1"), Courses.objects.get(id="3")],
        [Courses.objects.get(id="2"), Courses.objects.get(id="4")],
        [Courses.objects.get(id="3"), Courses.objects.get(id="5")],
        [Courses.objects.get(id="4"), Courses.objects.get(id="6")],
        [Courses.objects.get(id="5"), Courses.objects.get(id="7")],
        [Courses.objects.get(id="6"), Courses.objects.get(id="8")],
        [Courses.objects.get(id="1"), Courses.objects.get(id="8")],
    ]

    for i in range(1, 7):
        teacher = CourseTeachers.objects.get(id=i)
        teacher.course.set(courses[i - 1])


def reverse_func(apps, schema_editor):
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    CourseTeachers.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0004_data_lessons"),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
