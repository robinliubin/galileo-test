"""Shared helpers for scenario agents built from the Galileo quickstart flow."""

from __future__ import annotations

from dataclasses import dataclass

from galileo import galileo_context
from galileo.config import GalileoPythonConfig
from galileo.log_streams import create_log_stream
from galileo.projects import delete_project


@dataclass(slots=True)
class ScenarioAgent:
    name: str
    description: str
    project_name: str
    log_stream_name: str

    def bootstrap(self) -> str:
        """Initialize Galileo using the quickstart pattern."""
        galileo_context.init(project=self.project_name, log_stream=self.log_stream_name)
        try:
            create_log_stream(name=self.log_stream_name, project_name=self.project_name)
        except Exception:
            pass
        return self._console_links()

    def _console_links(self) -> str:
        try:
            config = GalileoPythonConfig.get()
            logger = galileo_context.get_logger_instance()
            project_id = getattr(logger, "project_id", None)
            log_stream_id = getattr(logger, "log_stream_id", None)
            if not project_id or not log_stream_id:
                return "Galileo context initialized"
            project_url = f"{config.console_url}project/{project_id}"
            log_stream_url = f"{project_url}/log-streams/{log_stream_id}"
            return f"Project: {project_url} | Log stream: {log_stream_url}"
        except Exception:
            return "Galileo context initialized"

    def cleanup(self) -> None:
        try:
            delete_project(name=self.project_name)
        except Exception:
            pass
