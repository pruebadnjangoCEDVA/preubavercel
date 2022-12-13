# Generated by Django 4.1.1 on 2022-11-17 19:10

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
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(blank=True, max_length=100)),
                ('activo_por_pagos', models.BooleanField(default=False, verbose_name='Status')),
                ('nombreA', models.CharField(max_length=100)),
                ('snombreA', models.CharField(blank=True, max_length=100, null=True)),
                ('apellidoPA', models.CharField(max_length=100)),
                ('apellidoMA', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('convenio', models.CharField(choices=[('p', 'Seleccione opción'), ('SI', 'Si'), ('NO', 'No')], default='p', max_length=800)),
                ('inicioCurso', models.DateField()),
                ('finalCurso', models.DateField()),
                ('observaciones', models.CharField(max_length=1000)),
                ('certificado', models.BooleanField(default=False, verbose_name='Certificado')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'alumno',
                'verbose_name_plural': 'alumnos',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('lote', models.IntegerField()),
                ('manzana', models.IntegerField()),
                ('colonia', models.CharField(max_length=100)),
                ('delegacionMunicipio', models.CharField(max_length=100)),
                ('codigopostal', models.IntegerField()),
                ('ciudadOestado', models.CharField(choices=[('p', 'Seleccione opción'), ('Estado de México', 'Estado de México'), ('Ciudad de México', 'Ciudad de México')], default='p', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'direccion',
                'verbose_name_plural': 'direcciones',
            },
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantel', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'plantel',
                'verbose_name_plural': 'planteles',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreT', models.CharField(max_length=100)),
                ('apellidoPT', models.CharField(max_length=100)),
                ('apellidoMT', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('padreT', models.CharField(choices=[('p', 'Seleccione opción'), ('Padre', 'Padre'), ('Madre', 'Madre'), ('Tutor', 'Tutor')], default='p', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tutor',
                'verbose_name_plural': 'tutores',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PagoRegistrado', models.CharField(blank=True, max_length=120, null=True)),
                ('folio', models.IntegerField()),
                ('Estado_pago', models.BooleanField(blank=True, default=False, null=True, verbose_name='revicion')),
                ('tipoPago', models.CharField(max_length=100)),
                ('monto', models.IntegerField()),
                ('Findepagos', models.BooleanField(default=False, verbose_name='Concluido')),
                ('fechaPago', models.DateField()),
                ('mesPagado', models.CharField(blank=True, max_length=12, null=True)),
                ('horapago', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories7', to='Cedva1.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreE', models.CharField(choices=[('p', 'Seleccione opción'), ('Bachillerato con mecánica automotriz', 'Bachillerato con mecánica automotriz'), ('Mécanica en motocicletas', 'Mécanica en motocicletas'), ('Mécanica a gasolina', 'Mécanica a gasolina'), ('Mécanica a diésel', 'Mécanica a diésel'), ('Ingenieria en Mecánica Automotriz', 'Ingenieria en Mecánica Automotriz')], default='p', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('idEscuela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories8', to='Cedva1.escuela')),
            ],
            options={
                'verbose_name': 'especialidad',
                'verbose_name_plural': 'especialidades',
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories2', to='Cedva1.direccion'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='especialidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories1', to='Cedva1.especialidad'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories3', to='Cedva1.tutor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoP', models.CharField(max_length=100)),
                ('apellidoM', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('escuela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories5', to='Cedva1.escuela')),
                ('usuarioA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories6', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'administrador',
                'verbose_name_plural': 'administradores',
            },
        ),
    ]
