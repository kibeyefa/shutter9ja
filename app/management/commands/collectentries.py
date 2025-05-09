from django.core.management.base import BaseCommand
from app.models import Entry
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Exports photo entries to an Excel file.'

    def handle(self, *args, **kwargs):
        # Fetch entries from the database
        entries = Entry.objects.values(
            'full_name',
            'phone',
            'instagram_username',
            'email'
        )

        if not entries:
            self.stdout.write(self.style.WARNING("No photo entries found."))
            return

        # Convert to pandas DataFrame
        df = pd.DataFrame(list(entries))

        # Export to Excel
        output_file = 'photoentries_export.xlsx'
        df.to_excel(output_file, index=False)

        self.stdout.write(self.style.SUCCESS(f"Exported {len(df)} entries to '{output_file}'"))
