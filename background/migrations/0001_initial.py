# Generated by Django 4.2.13 on 2025-01-16 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='backgrounds/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backgrounds', to='campaign.campaign')),
            ],
        ),
    ]
