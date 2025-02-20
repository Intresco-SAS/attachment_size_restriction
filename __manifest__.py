# See LICENSE file for full copyright and licensing details.

{
    "name": "Attachment Size Restriction",
    "version": "15.0.1.0.0",
    "summary": "Restrict to uploading the larger file than the configured.",
    "category": "Mail",
    "depends": ["mail"],
    "author": "BizzAppDev",
    "website": "http://www.bizzappdev.com",
    "license": "LGPL-3",
    "data": [
        "data/ir_config_parameter_data.xml",
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "attachment_size_restriction"
            "/static/src/components/file_uploader/file_uploader.esm.js",
        ]
    },
    "images": ["images/attachment_size_restriction.png"],
    "installable": True,
    "application": True,
}
