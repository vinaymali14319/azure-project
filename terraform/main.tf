# Provider Configuration
provider "azurerm" {
  features {}  
 
}

# ==================== VARIABLES ====================

# Define variables for resource group names, locations, and resource names
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

variable "dev_adf_name" {
  default = "dev-vinay-adf"
}

variable "prod_adf_name" {
  default = "prod-vinay-adf"
}

variable "dev_adls_name" {
  default = "devvinaymaliadls"     # must be unique
}

variable "prod_adls_name" {
  default = "prodvinaymaliadls"     # must be unique
}

variable "dev_databricks_name" {
  default = "dev-vinay-databricks"
}

variable "prod_databricks_name" {
  default = "prod-vinay-databricks"
}

variable "databricks_sku" {
  default = "premium"         
}

# ==================== DEV Environment ====================

# Create Resource Group for Dev
resource "azurerm_resource_group" "dev_rg" {
  name     = var.dev_rg_name
  location = var.dev_location
}

# Create Azure Data Factory for Dev
resource "azurerm_data_factory" "dev_adf" {
  name                = var.dev_adf_name
  resource_group_name = azurerm_resource_group.dev_rg.name
  location            = azurerm_resource_group.dev_rg.location
}

# Create ADLS Gen2 Storage Account for Dev
resource "azurerm_storage_account" "dev_adls" {
  name                     = var.dev_adls_name                   
  resource_group_name      = azurerm_resource_group.dev_rg.name
  location                 = azurerm_resource_group.dev_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled = true
}

# Create Databricks Workspace for Dev
resource "azurerm_databricks_workspace" "dev_databricks" {
  name                = var.dev_databricks_name
  resource_group_name = azurerm_resource_group.dev_rg.name
  location            = azurerm_resource_group.dev_rg.location
  sku                 = var.databricks_sku
}

# ==================== PROD Environment ====================

# Create Resource Group for Prod
resource "azurerm_resource_group" "prod_rg" {
  name     = var.prod_rg_name
  location = var.prod_location
}

# Create Azure Data Factory for Prod
resource "azurerm_data_factory" "prod_adf" {
  name                = var.prod_adf_name
  resource_group_name = azurerm_resource_group.prod_rg.name
  location            = azurerm_resource_group.prod_rg.location
}

# Create ADLS Gen2 Storage Account for Prod
resource "azurerm_storage_account" "prod_adls" {
  name                     = var.prod_adls_name                  
  resource_group_name      = azurerm_resource_group.prod_rg.name
  location                 = azurerm_resource_group.prod_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled = true
}

# Create Databricks Workspace for Prod
resource "azurerm_databricks_workspace" "prod_databricks" {
  name                = var.prod_databricks_name
  resource_group_name = azurerm_resource_group.prod_rg.name
  location            = azurerm_resource_group.prod_rg.location
  sku                 = var.databricks_sku
}
