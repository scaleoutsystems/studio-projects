# Generated by Django 4.0 on 2021-12-13 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('password', models.CharField(blank=True, default='', max_length=100)),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='MLFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mlflow_url', models.CharField(max_length=512)),
                ('name', models.CharField(max_length=512)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mlflowobj', to='apps.appinstance')),
                ('basic_auth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.basicauth')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('clone_url', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=512)),
                ('project_image', models.ImageField(blank=True, default=None, null=True, upload_to='projects/images/')),
                ('slug', models.CharField(max_length=512, unique=True)),
                ('status', models.CharField(blank=True, default='active', max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.CharField(blank=True, max_length=2048, null=True)),
                ('project_key', models.CharField(max_length=512)),
                ('project_secret', models.CharField(max_length=512)),
                ('repository', models.CharField(blank=True, max_length=512, null=True)),
                ('repository_imported', models.BooleanField(default=False)),
                ('authorized', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('mlflow', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_mlflow', to='projects.mlflow')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='S3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_key', models.CharField(max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=512)),
                ('name', models.CharField(max_length=512)),
                ('region', models.CharField(blank=True, default='', max_length=512)),
                ('secret_key', models.CharField(max_length=512)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s3obj', to='apps.appinstance')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s3_project', to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=512)),
                ('status', models.CharField(max_length=10)),
                ('app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.appinstance')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projecttemplates/images/')),
                ('name', models.CharField(max_length=512)),
                ('revision', models.IntegerField(default=1)),
                ('slug', models.CharField(default='', max_length=512)),
                ('template', models.JSONField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('slug', 'revision')},
            },
        ),
        migrations.CreateModel(
            name='ProjectLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=512)),
                ('headline', models.CharField(max_length=256)),
                ('module', models.CharField(choices=[('DE', 'deployments'), ('LA', 'labs'), ('MO', 'models'), ('PR', 'projects'), ('RE', 'reports'), ('UN', 'undefined')], default='UN', max_length=2)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='s3storage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_s3', to='projects.s3'),
        ),
        migrations.AddField(
            model_name='mlflow',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mlflow_project', to='projects.project'),
        ),
        migrations.AddField(
            model_name='mlflow',
            name='s3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.s3'),
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cpu_lim', models.TextField(blank=True, default='1000m', null=True)),
                ('gpu_lim', models.TextField(blank=True, default='0', null=True)),
                ('ephmem_lim', models.TextField(blank=True, default='200Mi', null=True)),
                ('mem_lim', models.TextField(blank=True, default='3Gi', null=True)),
                ('cpu_req', models.TextField(blank=True, default='200m', null=True)),
                ('gpu_req', models.TextField(blank=True, default='0', null=True)),
                ('ephmem_req', models.TextField(blank=True, default='200Mi', null=True)),
                ('mem_req', models.TextField(blank=True, default='0.5Gi', null=True)),
                ('name', models.CharField(max_length=512)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('repository', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.CharField(max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.apps')),
                ('appenv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='envobj', to='apps.appinstance')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('registry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='environments', to='apps.appinstance')),
            ],
        ),
        migrations.AddField(
            model_name='basicauth',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ba_project', to='projects.project'),
        ),
    ]
