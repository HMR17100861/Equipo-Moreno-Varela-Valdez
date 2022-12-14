# Generated by Django 4.1.2 on 2022-10-26 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('motor', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('origen', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=255)),
                ('no_calle', models.IntegerField()),
                ('pais', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('domicilio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.domicilio')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.carro')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numFactura', models.CharField(max_length=255)),
                ('costo', models.IntegerField()),
                ('compra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.carro')),
                ('comprador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.persona')),
            ],
        ),
    ]
