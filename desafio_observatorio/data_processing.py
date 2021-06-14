""" Módulo de processamento de dados """
import os
import requests

import pandas as pd

from helpers import STATES, INDICATOR_OPTIONS, API_URL, LOCAL_FILES_DIR


def hit_api(endpoint: str) -> dict:
    """Wrapper de uma requisição para pedir dados a API"""
    headers = {
        "accept": "application/json",
    }

    response = requests.get(API_URL + endpoint, headers=headers)

    return response.json()


def api_get_ncm_code_listing() -> dict:
    """Requisita da API a listagem de códigos NCM"""

    return hit_api("cod_ncm_listing/")


def api_get_state_contribution() -> dict:
    """Requisita da API dados sobre a contribuição percentual por estado"""

    return hit_api("states_contribution/")


def api_get_operation_statistics(year: int, operation: str, cod_ncm: int) -> dict:
    """Obtém estatísticas sobre operações financeiras"""

    operation_key = OPERATION_OPTIONS[operation]
    return hit_api(f"operation_statistics/{year}/{operation_key}/{cod_ncm}")


def api_get_via_statistics_statistics(year: int, operation: str, cod_ncm: int) -> dict:
    """Obtém dados sobre uso da via"""

    operation_key = OPERATION_OPTIONS[operation]
    return hit_api(f"via_statistics/{year}/{operation_key}/{cod_ncm}")
