# from .client import client
from .common_utils import parse_date_to_string


def list_credentials(self, _for=''):
    url = self.endpoint + f"/creds?for={_for}"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def post_credentials(
        self, name,
        iam_cred_type,
        default_ingest_team_id,
        provider_id,
        access_key_id='',
        discoverable='',
        secret_access_key='',
        partition='',
        iam_role_external_id='',
        iam_role_arn='',
        az_subscription_id='',
        az_tenant_id='',
        az_client_id='',
        az_client_secret='',
        az_access_key_expire_date='',
        az_enrollment_id='',
        az_primary_access_key='',
        az_primary_access_key_expire_date='',
        az_secondary_access_key='',
        az_secondary_access_key_expire_date='',
        gcp_sa_key='',
        gcp_project_id=''
):
    az_access_key_expire_date = parse_date_to_string(
        az_access_key_expire_date)
    az_primary_access_key_expire_date = parse_date_to_string(
        az_primary_access_key_expire_date)
    az_secondary_access_key_expire_date = parse_date_to_string(
        az_secondary_access_key_expire_date)

    url = self.endpoint + "/creds"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    body_keys = {
        "name",
        "iam_cred_type",
        "default_ingest_team_id",
        "provider_id",
        "access_key_id",
        "discoverable",
        "secret_access_key",
        "partition",
        "iam_role_external_id",
        "iam_role_arn",
        "az_subscription_id",
        "az_tenant_id",
        "az_client_id",
        "az_client_secret",
        "az_access_key_expire_date",
        "az_enrollment_id",
        "az_primary_access_key",
        "az_primary_access_key_expire_date",
        "az_secondary_access_key",
        "az_secondary_access_key_expire_date",
        "gcp_sa_key",
        "gcp_project_id",
    }

    local_vars = locals()
    body = {k: local_vars[k] for k in body_keys if local_vars[k]}

    response = self.request("POST", url, headers, body)

    return response


def disable_credential(self, id):
    url = self.endpoint + f"/creds/disable/{id}"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    response = self.request("PUT", url, headers)

    return response


def update_credential(
        self, id, name,
        iam_cred_type,
        default_ingest_team_id,
        provider_id,
        access_key_id='',
        discoverable='',
        secret_access_key='',
        partition='',
        iam_role_external_id='',
        iam_role_arn='',
        az_subscription_id='',
        az_tenant_id='',
        az_client_id='',
        az_client_secret='',
        az_access_key_expire_date='',
        az_enrollment_id='',
        az_primary_access_key='',
        az_primary_access_key_expire_date='',
        az_secondary_access_key='',
        az_secondary_access_key_expire_date='',
        gcp_sa_key='',
        gcp_project_id=''
):

    az_access_key_expire_date = parse_date_to_string(
        az_access_key_expire_date)
    az_primary_access_key_expire_date = parse_date_to_string(
        az_primary_access_key_expire_date)
    az_secondary_access_key_expire_date = parse_date_to_string(
        az_secondary_access_key_expire_date)

    url = self.endpoint + f"/creds/{id}"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    body_keys = {
        "name",
        "iam_cred_type",
        "default_ingest_team_id",
        "provider_id",
        "access_key_id",
        "discoverable",
        "secret_access_key",
        "partition",
        "iam_role_external_id",
        "iam_role_arn",
        "az_subscription_id",
        "az_tenant_id",
        "az_client_id",
        "az_client_secret",
        "az_access_key_expire_date",
        "az_enrollment_id",
        "az_primary_access_key",
        "az_primary_access_key_expire_date",
        "az_secondary_access_key",
        "az_secondary_access_key_expire_date",
        "gcp_sa_key",
        "gcp_project_id",
    }

    local_vars = locals()
    body = {k: local_vars[k] for k in body_keys if local_vars[k]}

    response = self.request("PUT", url, headers, body)

    return response


def delete_credential(
        self, id, name,
        iam_cred_type,
        default_ingest_team_id,
        provider_id,
        access_key_id='',
        discoverable='',
        secret_access_key='',
        partition='',
        iam_role_external_id='',
        iam_role_arn='',
        az_subscription_id='',
        az_tenant_id='',
        az_client_id='',
        az_client_secret='',
        az_access_key_expire_date='',
        az_enrollment_id='',
        az_primary_access_key='',
        az_primary_access_key_expire_date='',
        az_secondary_access_key='',
        az_secondary_access_key_expire_date='',
        gcp_sa_key='',
        gcp_project_id=''
):

    az_access_key_expire_date = parse_date_to_string(
        az_access_key_expire_date)
    az_primary_access_key_expire_date = parse_date_to_string(
        az_primary_access_key_expire_date)
    az_secondary_access_key_expire_date = parse_date_to_string(
        az_secondary_access_key_expire_date)

    url = self.endpoint + f"/creds/{id}"

    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': self.auth_token
    }

    body_keys = {
        "name",
        "iam_cred_type",
        "default_ingest_team_id",
        "provider_id",
        "access_key_id",
        "discoverable",
        "secret_access_key",
        "partition",
        "iam_role_external_id",
        "iam_role_arn",
        "az_subscription_id",
        "az_tenant_id",
        "az_client_id",
        "az_client_secret",
        "az_access_key_expire_date",
        "az_enrollment_id",
        "az_primary_access_key",
        "az_primary_access_key_expire_date",
        "az_secondary_access_key",
        "az_secondary_access_key_expire_date",
        "gcp_sa_key",
        "gcp_project_id",
    }

    local_vars = locals()
    body = {k: local_vars[k] for k in body_keys if local_vars[k]}

    response = self.request("DELETE", url, headers, body)

    return response


def get_example_aws_policy(self):
    url = self.endpoint + "/creds/example-aws-policy"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def get_example_azure_policy(self):
    url = self.endpoint + "/creds/example-azure-role"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def get_credential_ingestion(self, id):
    url = self.endpoint + f"/creds/ingest/{id}"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("GET", url, headers)

    return response


def start_credential_ingestion(self, id, force=False):
    url = self.endpoint + f"/creds/ingest/{id}?force={str(force).lower()}"

    headers = {
        'X-Auth-Token': self.auth_token
    }

    response = self.request("POST", url, headers)

    return response
