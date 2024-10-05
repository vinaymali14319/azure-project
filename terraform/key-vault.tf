variable "global_rg_name" {
  default = "global-rg"  
}

variable "global_key_vault_name" {
  default = "global-vinay-key-vault"  
}



data "azurerm_key_vault" "global_keyvault" {
  name                = var.global_key_vault_name
  resource_group_name = var.global_rg_name
}

data "azurerm_key_vault_secret" "subscription_id" {
  name          = "subscription-id"  
  key_vault_id = data.azurerm_key_vault.global_keyvault.id
}

data "azurerm_key_vault_secret" "client_id" {
  name          = "client-id"
  key_vault_id = data.azurerm_key_vault.global_keyvault.id
}

data "azurerm_key_vault_secret" "client_secret" {
  name          = "client-secret" 
  key_vault_id = data.azurerm_key_vault.global_keyvault.id
}

data "azurerm_key_vault_secret" "tenant_id" {
  name          = "tenant-id"  
  key_vault_id = data.azurerm_key_vault.global_keyvault.id
}



provider "azurerm" {
  features {}  
  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  tenant_id       = var.tenant_id
}


variable "dev_location" {
  default = "South India"  
}

variable "prod_location" {
  default = "South India"  
}

variable "dev_rg_name" {
  default = "dev-vinay-rg"
}

variable "prod_rg_name" {
  default = "prod-vinay-rg"
}

variable "dev_keyvault_name" {
  default = "dev-keyvault-vinay"  
}

variable "prod_keyvault_name" {
  default = "prod-keyvault-vinay"  
}


# Create Resource Group for Development
resource "azurerm_resource_group" "dev_rg" {
  name     = var.dev_rg_name
  location = var.dev_location
}

# Create Resource Group for Production
resource "azurerm_resource_group" "prod_rg" {
  name     = var.prod_rg_name
  location = var.prod_location
}

# Create Azure Key Vault for Development
resource "azurerm_key_vault" "dev_keyvault" {
  name                = var.dev_keyvault_name
  location            = azurerm_resource_group.dev_rg.location
  resource_group_name = azurerm_resource_group.dev_rg.name
  sku_name            = "standard"

}

# Create Azure Key Vault for Production
resource "azurerm_key_vault" "prod_keyvault" {
  name                = var.prod_keyvault_name
  location            = azurerm_resource_group.prod_rg.location
  resource_group_name = azurerm_resource_group.prod_rg.name
  sku_name            = "standard"

}
