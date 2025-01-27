from django.db import migrations

def create_default_tags(apps, schema_editor):
    Tag = apps.get_model('gallery', 'Tag')
    default_tags = ['Wesele', 'Urodziny', 'Chrzciny']
    for tag_name in default_tags:
        Tag.objects.get_or_create(name=tag_name)

class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_tag_delete_video_photo_tags'),
    ]

    operations = [
        migrations.RunPython(create_default_tags),
    ]