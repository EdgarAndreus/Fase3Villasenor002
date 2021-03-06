# Generated by Django 3.1.2 on 2020-11-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20201102_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(null=True),
        ),
    ]
