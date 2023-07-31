# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # New Python User Overview
# MAGIC
# MAGIC The [sas_interop](https://github.com/balbarka/sas_interop) is focused on the interoperability tools that exist for SAS to connect to Databricks and vise-versa. These tools and connection pattern are necessary applications and/or business units that require both platforms. Provided here are the **connectivity** patterns:
# MAGIC
# MAGIC | Connect to Databricks </br> from SAS | Connect to Databricks </br> from Jupyter | Shared Storage for SAS </br> and Databricks | Connect to SAS </br> from Databricks |
# MAGIC | ------------------------------------ | ---------------------------------------- | ------------------------------------------ | ------------------------------------ |
# MAGIC | <img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../02-SAS-ACCESS_JDBC" target="_blank">02-SAS-ACCESS_JDBC</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/02-SAS-ACCESS_JDBC_cdata.sas" target="_blank">02-SAS-ACCESS_JDBC_cdata.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/02-SAS-ACCESS_JDBC_databricks.sas" target="_blank">02-SAS-ACCESS_JDBC_databricks.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../03-SAS-ACCESS_ODBC" target="_blank">03-SAS-ACCESS_ODBC</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/03-SAS-ACCESS_ODBC_databricks.sas" target="_blank">03-SAS-ACCESS_ODBC_databricks.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../04-SAS-ACCESS_Spark" target="_blank">04-SAS-ACCESS_Spark</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/04-SAS-ACCESS_Spark_databricks.sas" target="_blank">04-SAS-ACCESS_Spark_databricks.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/04-SAS-ACCESS_Spark_databricks_bl.sas" target="_blank">04-SAS-ACCESS_Spark_databricks_bl.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/04-SAS-ACCESS_Spark_cdata.sas" target="_blank">04-SAS-ACCESS_Spark_cdata.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/04-SAS-ACCESS_Spark_cdata_bl.sas" target="_blank">04-SAS-ACCESS_Spark_cdata_bl.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/04-SAS-ACCESS_Spark_CAS_cdata.sas" target="_blank">04-SAS-ACCESS_Spark_CAS_cdata.sas</a> | <img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/jupyter_logo_small.svg width=25 height=25> <a href="$../../nb/02-jdbc" target="_blank">02-jdbc</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/jupyter_logo_small.svg width=25 height=25> <a href="$../../nb/03-pyodbc" target="_blank">03-pyodbc</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/jupyter_logo_small.svg width=25 height=25> <a href="$../../nb/04-databricks-sql-connector" target="_blank">04-databricks-sql-connector</a> | <img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../05-External_Location_ADLS" target="_blank">05-External_Location_ADLS</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/05-External_Location_ADLS_filename.sas" target="_blank">05-External_Location_ADLS_filename.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../06-Text_FIles_ADLS" target="_blank">06-Text_FIles_ADLS</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/06-Text_Files_ADLS.sas" target="_blank">06-Text_Files_ADLS.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../07-ORC_ADLS" target="_blank">07-ORC_ADLS</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/07-ORC_ADLS.sas" target="_blank">07-ORC_ADLS.sas</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../08-Parquet_AWS" target="_blank">08-Parquet_AWS</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/sas_logo_small.png width=25 height=25> <a href="$../../sas/08-Parquet_ADLS.sas" target="_blank">08-Parquet_ADLS.sas</a> | <img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../01-SASPy" target="_blank">01_SASPy</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../09-sas7bdat_ADLS" target="_blank">09-sas7bdat_ADLS</a></br><img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$../11-SAS_Drivers" target="_blank">11-SAS_Drivers</a> |
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Introduction to Python Programming Language
# MAGIC
# MAGIC However, when introducing Databricks to SAS users with no prior python experience, it can be helpful to see how SAS functionality by SAS modules can be accomplished in Python. The focus in the following notebooks will be on Python (note necessarily Databricks) functionality.
# MAGIC
# MAGIC
# MAGIC | SAS Module | Python Functionality | description |
# MAGIC | ---------- | --------------- | ----------- |
# MAGIC | SAS Programming Language | <img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$./01_sas_language" target="_blank">01_sas_language</a> | SAS has its own programming language used for data manipulation, statistical analysis, and generating reports. This language includes </br> various data step functions and PROC (Procedure) steps that perform specific analytical tasks. |
# MAGIC | SAS Core </br> (Data Step) | <img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$./02_sas_core" target="_blank">02_sas_core</a> | This component includes the core components of SAS, such as the data step, PROC steps, and the macro language. SAS Base provides </br>essential functionality for data management and basic statistical analysis. |
# MAGIC | SAS Macro Language | <img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$./03_sas_macros" target="_blank">03_sas_macros</a> | SAS also includes a macro language that allows users to define and execute macro programs. </br>Macros are used to automate repetitive tasks and create dynamic code. </br> SAS Macro Language is technically part of SAS Core. |
# MAGIC | SAS/STAT | <img src=https://raw.githubusercontent.com/balbarka/sas_interop/main/ref/img/databricks_logo_small.svg width=25 height=25> <a href="$./04_sas_stat" target="_blank">04_sas_stat</a> | SAS/STAT module provides a wide range of statistical procedures and techniques for data analysis. </br> SAS/STAT is technically part of SAS Core. |
# MAGIC | SAS/SQL | 06_sas_sql | **INCOMPLETE** - This module enables users to perform SQL (Structured Query Language) operations within SAS, allowing for efficient data </br> manipulation and querying. </br> We'll look at both using SQL within python and Databricks Spark SQL API. |
# MAGIC | SAS/GRAPH | 05_sas_graph | **INCOMPLETE** - This module is used for creating various types of graphs and visualizations. |
# MAGIC | SAS/ACCESS | 07_sas_access | **INCOMPLETE** - This module facilitates access to data stored in external databases and files, enabling integration with other data sources. </br> While a lot of the sas_interop repo is focused on using SAS/ACCESS to connect to Databricks, </br> this section will show how python connects to other data sources. |
# MAGIC | SAS CAS | xx_xxxx | **INCOMPLETE** - SAS Cloud Analytic Services (CAS) is an advanced analytics processing engine that provides distributed, in-memory </br> processing for high-performance and parallel analysis of large-scale data in the SAS Viya platform. </br> This modules will include a light introduction to pyspark, the python API for Apache Spark. |
# MAGIC | SAS Model Manager |  | **TODO** - Intro to MLOps for python using MLFlow. |
# MAGIC
# MAGIC **NOTE**: There are a lot of differences in SAS / Python due to being different programming languages. However, there are also differences between SAS Cloud Managed Viya Platform and Databricks Platform. In SAS Viya, operations on Librefs are enhearently local and to run distributed compute you leverage CAS. In Databricks, Spark SQL leverages a metastore that has catalogs (or Hive), but the default interface is spark and is distributed. To do localized operations in Databricks, you must either access the Data at source with a non-distributed library or execute [toPandas](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.toPandas.html). Said differently: 
# MAGIC  * SAS data is inherently non-distributed and CAS provides distributed functionality
# MAGIC  * Databricks data is inherently distributed and includes a local python session for non-distributed python
# MAGIC  * If you know you will not be executing in a distributed fashion, consider using a [single-node cluster](https://learn.microsoft.com/en-us/azure/databricks/clusters/single-node).