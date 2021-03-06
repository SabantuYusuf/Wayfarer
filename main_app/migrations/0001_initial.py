from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=85, verbose_name='Current City')),
                ('prof_img', models.ImageField(blank=True, default='defaultpic.png', null=True, upload_to='images/', verbose_name='Profile Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_img', models.ImageField(default='stickynote.png', upload_to='images/')),
                ('content', models.CharField(blank=True, max_length=250, verbose_name='Content')),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('city_options', models.CharField(choices=[('1', 'San Francisco'), ('3', 'London'), ('2', 'Seattle'), ('4', 'Sydney')], default='1', max_length=2, verbose_name='City')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_app.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
