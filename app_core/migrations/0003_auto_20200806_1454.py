# Generated by Django 3.0.5 on 2020-08-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0002_auto_20200806_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('image', models.ImageField(null=True, upload_to='images/foto/')),
            ],
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('link', models.TextField()),
                ('banner', models.ImageField(null=True, upload_to='images/adverts/')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=60)),
                ('desc', models.TextField()),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('link', models.TextField()),
                ('logo', models.ImageField(null=True, upload_to='images/testimonials/')),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='certification',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/certifications/'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='image',
            field=models.ImageField(null=True, upload_to='images/certifications/'),
        ),
    ]
