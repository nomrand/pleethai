# Generated by Django 2.1.2 on 2019-06-08 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituent',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('order', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('japanese', models.CharField(max_length=511)),
                ('hiragana', models.CharField(max_length=511, null=True)),
                ('roman', models.CharField(max_length=511, null=True)),
                ('thai', models.CharField(max_length=511, null=True)),
                ('pronunciation_symbol', models.CharField(max_length=511, null=True)),
                ('pronunciation_kana', models.CharField(max_length=511, null=True)),
                ('english', models.CharField(max_length=511, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('japanese', models.CharField(max_length=127)),
                ('hiragana', models.CharField(max_length=127)),
                ('roman', models.CharField(max_length=127, null=True)),
                ('thai', models.CharField(max_length=127)),
                ('pronunciation_symbol', models.CharField(max_length=127, null=True)),
                ('pronunciation_kana', models.CharField(max_length=127, null=True)),
                ('order', models.PositiveSmallIntegerField(null=True)),
                ('english', models.CharField(max_length=127, null=True)),
                ('searchs', models.BigIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WordClass',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('thai', models.CharField(max_length=31, null=True)),
                ('japanese', models.CharField(max_length=31, null=True)),
                ('slug', models.SlugField(max_length=31, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='wordclass_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pleethai.WordClass'),
        ),
        migrations.AddField(
            model_name='constituent',
            name='example_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pleethai.Example'),
        ),
        migrations.AddField(
            model_name='constituent',
            name='word_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pleethai.Word'),
        ),
        migrations.AlterUniqueTogether(
            name='constituent',
            unique_together={('example_id', 'word_id', 'order')},
        ),
    ]
