from odoo import models, fields, api
import os
import uuid  # Import uuid library
class CustomFontIntegration(models.Model):
    _name = 'custom_font_integration'  # Modifier le nom ici
    _description = 'Custom Font Integration'

    name = fields.Char(string='Font Name', required=True)
    font_file = fields.Binary(string='Font File', required=True)

    def create_action(self):
        action = self.env['ir.actions.act_window'].create({
            'name': 'Custom Font Integration',
            'res_model': 'custom_font_integration',
            'view_mode': 'tree,form',
        })
        return action

    @api.model
    def create(self, values):
        if 'font_file' in values:
            # Generate a unique filename with extension
            filename, extension = os.path.splitext(values['name'])  # Split filename and extension
            unique_filename = f"{filename}_{uuid.uuid4()}{extension}"

            # Define the path within the static/fonts folder
            file_path = os.path.join('custom_font_integration', 'static', 'fonts', unique_filename)

            # Create the directory structure if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directories if needed

            # Write the font file content
            with open(file_path, 'wb') as file:  # Open in binary write mode
                file.write(values['font_file'].encode())  # Encode the string as bytes

        return super(CustomFontIntegration, self).create(values)
