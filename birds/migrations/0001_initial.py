# Generated by Django 2.1.4 on 2019-01-23 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom', models.CharField(max_length=40)),
                ('scientific_name', models.CharField(max_length=50)),
                ('scientific_name_author', models.CharField(max_length=40)),
                ('year', models.PositiveIntegerField()),
                ('accepted_as', models.CharField(max_length=70)),
                ('bengali_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('size_cm', models.PositiveIntegerField()),
                ('common_family', models.CharField(max_length=40)),
                ('common_group', models.CharField(max_length=40)),
                ('habit', models.CharField(max_length=20)),
                ('conservation_status', models.CharField(max_length=10)),
                ('reference', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birds_class', models.CharField(max_length=40)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='DistributionOfBengal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distribution_in_bengal', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=40)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='FamilyAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_author', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(max_length=40)),
                ('slug', models.SlugField()),
                ('family', models.ManyToManyField(help_text='Select Family Name...', to='birds.Family')),
            ],
        ),
        migrations.CreateModel(
            name='GenusAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus_author', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom', models.CharField(default='Animalia', max_length=40)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=40)),
                ('slug', models.SlugField()),
                ('bird_class', models.ManyToManyField(help_text='Select Class Name...', to='birds.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Phylum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phylum', models.CharField(max_length=40)),
                ('kingdom', models.CharField(default='Animalia', max_length=40)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='genus',
            name='genus_author',
            field=models.ManyToManyField(help_text='Select Genus Author name ... ', to='birds.GenusAuthor'),
        ),
        migrations.AddField(
            model_name='family',
            name='family_author',
            field=models.ManyToManyField(help_text='Select Family Author ...', to='birds.FamilyAuthor'),
        ),
        migrations.AddField(
            model_name='family',
            name='order',
            field=models.ManyToManyField(help_text='Select Order Name...', to='birds.Order'),
        ),
        migrations.AddField(
            model_name='class',
            name='phylum',
            field=models.ManyToManyField(help_text='Select Phylum Name...', to='birds.Phylum'),
        ),
        migrations.AddField(
            model_name='birds',
            name='bird_class',
            field=models.ManyToManyField(help_text='Select Class Name...', to='birds.Class'),
        ),
        migrations.AddField(
            model_name='birds',
            name='distribution_in_bengal',
            field=models.ManyToManyField(help_text='Select Place ..', to='birds.DistributionOfBengal'),
        ),
        migrations.AddField(
            model_name='birds',
            name='family',
            field=models.ManyToManyField(help_text='Select Family Name...', to='birds.Family'),
        ),
        migrations.AddField(
            model_name='birds',
            name='family_author',
            field=models.ManyToManyField(help_text='Select Family Author name ... ', to='birds.FamilyAuthor'),
        ),
        migrations.AddField(
            model_name='birds',
            name='genus',
            field=models.ManyToManyField(help_text='Select Genus name ..', to='birds.Genus'),
        ),
        migrations.AddField(
            model_name='birds',
            name='genus_author',
            field=models.ManyToManyField(help_text='Select Genus Author name ... ', to='birds.GenusAuthor'),
        ),
        migrations.AddField(
            model_name='birds',
            name='order',
            field=models.ManyToManyField(help_text='Select Order Name...', to='birds.Order'),
        ),
        migrations.AddField(
            model_name='birds',
            name='phylum',
            field=models.ManyToManyField(help_text='Select Phylum Name...', to='birds.Phylum'),
        ),
        migrations.AddField(
            model_name='birds',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birds.Status'),
        ),
    ]
