# Generated by Django 5.1.2 on 2024-10-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_prodocts_brand_prodocts_quantityinstock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
    ]
