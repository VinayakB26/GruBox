# Generated by Django 2.2.6 on 2019-10-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Class', models.IntegerField()),
                ('RollNo', models.IntegerField()),
                ('Semester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubjectMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.IntegerField()),
                ('Class', models.IntegerField()),
                ('SubjectId', models.IntegerField()),
                ('Marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubjectName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectId', models.IntegerField()),
                ('SubjectName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TopperName', models.CharField(max_length=61)),
                ('RollNo', models.IntegerField()),
                ('Class', models.IntegerField()),
                ('TotalMarks', models.IntegerField()),
            ],
        ),
    ]
