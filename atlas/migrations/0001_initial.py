# Generated by Django 5.1.5 on 2025-02-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('stamping', models.CharField(choices=[('420_inner', '420 inner'), ('420_outer', '420 outer'), ('428_inner', '428 inner'), ('428_outer', '428 outer'), ('cam_inner', 'cam inner'), ('cam_outer', 'cam outer')], max_length=255)),
                ('stamping_quantity', models.IntegerField()),
                ('cold_forming', models.CharField(choices=[('420_bush', '420 bush'), ('420_roller', '420 roller'), ('428_bush', '428 bush'), ('428_roller', '428 roller'), ('cam_bush', 'cam bush')], max_length=255)),
                ('cold_forming_quantity', models.IntegerField()),
                ('pin_cutting', models.CharField(choices=[('420_pin', '420 pin'), ('428_pin', '428 pin'), ('cam_pin', 'cam pin')], max_length=255)),
                ('pin_cutting_quantity', models.IntegerField()),
                ('polishing', models.CharField(choices=[('420_inner', '420 inner'), ('420_outer', '420 outer'), ('428_inner', '428 inner'), ('428_outer', '428 outer'), ('cam_inner', 'cam inner'), ('cam_outer', 'cam outer'), ('420_pin', '420 pin'), ('428_pin', '428 pin'), ('cam_pin', 'cam pin'), ('420_bush', '420 bush'), ('420_roller', '420 roller'), ('428_bush', '428 bush'), ('428_roller', '428 roller'), ('cam_bush', 'cam bush')], max_length=255)),
                ('polishing_quantity', models.IntegerField()),
                ('drying_1', models.CharField(choices=[('cam_inner', 'cam inner'), ('cam_outer', 'cam outer'), ('cam_pin', 'cam pin'), ('cam_bush', 'cam bush')], max_length=255)),
                ('drying_1_quantity', models.IntegerField()),
                ('drying_2', models.CharField(choices=[('420_inner', '420 inner'), ('420_outer', '420 outer'), ('428_inner', '428 inner'), ('428_outer', '428 outer'), ('420_pin', '420 pin'), ('428_pin', '428 pin'), ('420_bush', '420 bush'), ('420_roller', '420 roller'), ('428_bush', '428 bush'), ('428_roller', '428 roller')], max_length=255)),
                ('drying_2_quantity', models.IntegerField()),
                ('at_furnace', models.CharField(choices=[('420_inner', '420 inner'), ('420_outer', '420 outer'), ('428_inner', '428 inner'), ('428_outer', '428 outer')], max_length=255)),
                ('at_furnace_quantity', models.IntegerField()),
                ('cp_furnace', models.CharField(choices=[('cam_inner', 'cam inner'), ('cam_outer', 'cam outer'), ('420_pin', '420 pin'), ('428_pin', '428 pin'), ('cam_pin', 'cam pin'), ('420_bush', '420 bush'), ('420_roller', '420 roller'), ('428_bush', '428 bush'), ('428_roller', '428 roller'), ('cam_bush', 'cam bush')], max_length=255)),
                ('cp_furnace_quantity', models.IntegerField()),
                ('shot_peening', models.CharField(choices=[('420_inner', '420 inner'), ('420_outer', '420 outer'), ('428_inner', '428 inner'), ('428_outer', '428 outer')], max_length=255)),
                ('shot_peening_quantity', models.IntegerField()),
                ('tumbler_polishing', models.CharField(choices=[('cam_inner', 'cam inner'), ('cam_outer', 'cam outer'), ('cam_pin', 'cam pin'), ('cam_bush', 'cam bush')], max_length=255)),
                ('tumbler_polishing_quantity', models.IntegerField()),
                ('drying', models.CharField(choices=[('cam_inner', 'cam inner'), ('cam_outer', 'cam outer'), ('cam_pin', 'cam pin'), ('cam_bush', 'cam bush')], max_length=255)),
                ('drying_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('420', '420'), ('428', '428'), ('CAM', 'CAM')], max_length=50)),
                ('material', models.CharField(choices=[('SAE1050 (1.2 × 104.2)', 'SAE1050 (1.2 × 104.2)'), ('SAE1050 (1.2 × 1219)', 'SAE1050 (1.2 × 1219)'), ('SAE1050 (1.2 × 110.4)', 'SAE1050 (1.2 × 110.4)'), ('SAE1050 (1.5 × 111.3)', 'SAE1050 (1.5 × 111.3)'), ('SAE1050 (1.5 × 1219)', 'SAE1050 (1.5 × 1219)'), ('SAE1050 (1.5 × 115.7)', 'SAE1050 (1.5 × 115.7)'), ('SAE1045 (0.72 × 98)', 'SAE1045 (0.72 × 98)'), ('SAE1045 (0.72 × 1000)', 'SAE1045 (0.72 × 1000)'), ('SAE1045 (0.72 × 95.5)', 'SAE1045 (0.72 × 95.5)'), ('Steel Wire SCR420 (φ3.97)', 'Steel Wire SCR420 (φ3.97)'), ('Steel Wire SCR420 (φ4.51)', 'Steel Wire SCR420 (φ4.51)'), ('Steel Wire SAE1018 (φ5.00)', 'Steel Wire SAE1018 (φ5.00)'), ('Steel Wire SAE1018 (φ7.50)', 'Steel Wire SAE1018 (φ7.50)'), ('Steel Wire SAE1018 (φ6.03)', 'Steel Wire SAE1018 (φ6.03)'), ('Steel Wire SAE1018 (φ8.10)', 'Steel Wire SAE1018 (φ8.10)'), ('Steel Wire SCM420 (φ2.30)', 'Steel Wire SCM420 (φ2.30)'), ('Cold Rolled Steel SAE 8620 (0.435 × 4.72)', 'Cold Rolled Steel SAE 8620 (0.435 × 4.72)')], max_length=255)),
                ('part', models.CharField(choices=[('Inner Plate', 'Inner Plate'), ('Outer Plate', 'Outer Plate'), ('Pin', 'Pin'), ('Bush', 'Bush'), ('Roller', 'Roller')], max_length=50)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Targets',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('_420_target', models.IntegerField()),
                ('_428_target', models.IntegerField()),
                ('cam_target', models.IntegerField()),
            ],
        ),
    ]
