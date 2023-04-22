# Generated by Django 4.1.4 on 2023-03-26 13:44

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_feature_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='demo_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_total',
        ),
        migrations.AddField(
            model_name='project',
            name='feature_video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='quick_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='feature_image',
            field=models.ImageField(blank=True, default='coming_soon.png', null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]