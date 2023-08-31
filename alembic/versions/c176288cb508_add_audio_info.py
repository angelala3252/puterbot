"""Add audio info.

Revision ID: c176288cb508
Revises: 8713b142f5de
Create Date: 2023-08-31 00:25:04.889325

"""
import sqlalchemy as sa

from alembic import op
from openadapt.models import ForceFloat

# revision identifiers, used by Alembic.
revision = "c176288cb508"
down_revision = "8713b142f5de"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "audio_info",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("flac_data", sa.LargeBinary(), nullable=True),
        sa.Column("transcribed_text", sa.String(), nullable=True),
        sa.Column(
            "recording_timestamp",
            ForceFloat(precision=10, scale=2, asdecimal=False),
            nullable=True,
        ),
        sa.Column("sample_rate", sa.Integer(), nullable=True),
        sa.Column("words_with_timestamps", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["recording_timestamp"],
            ["recording.timestamp"],
            name=op.f("fk_audio_info_recording_timestamp_recording"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_audio_info")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("audio_info")
    # ### end Alembic commands ###