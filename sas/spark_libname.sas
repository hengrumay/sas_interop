/* Tests LIBNAME Statement for Spark */
/* https://go.documentation.sas.com/doc/en/pgmsascdc/v_037/acreldb/n1udyznblny75qn1x7ng2y4wahxf.htm */

* %let HTTP_PATH=WAREHOUSE_PATH;
%let HTTP_PATH=&CLUSTER_PATH;

options azuretenantid="&AZ_TENANT_ID";

libname cdata clear;
libname cdata spark
  driverClass="cdata.jdbc.databricks.DatabricksDriver"
  bulkload=NO 
  url='jdbc:databricks://&DBR_HOST:443;
       HTTPPath=&CLUSTER_PATH;
       Database=default;
       QueryPassthrough=true;
       Token=&DBR_TOKEN;';

libname cdata_bl clear;
libname cdata_bl spark 
  classpath="/export/sas-viya/data/drivers/"
  driverClass="cdata.jdbc.databricks.DatabricksDriver"
  bulkload=yes
  bl_applicationid='&ADLS_APPLICATION_ID'
  bl_accountname='&ADLS_ACCOUNT_NAME'
  bl_filesystem='&ADLS_FILESYSTEM'
  url='jdbc:databricks://&DBR_HOST:443;
       HTTPPath=&CLUSTER_PATH;
       Database=default;
       QueryPassthrough=true;DefaultColumnSize=255;
       Token=&DBR_TOKEN;';

libname dbx clear;
libname dbx spark
  classpath="/export/sas-viya/data/drivers/"
  driverClass="com.databricks.client.jdbc.Driver"
  bulkload=NO 
  url='jdbc:spark://&DBR_HOST:443;
       HTTPPath=&CLUSTER_PATH;
       Database=default;
       QueryPassthrough=true;'
  user=token
  password=&DBR_TOKEN; 

libname dbx_bl clear;
libname dbx_bl spark
  classpath="/export/sas-viya/data/drivers/"
  driverClass="com.databricks.client.jdbc.Driver"
  bulkload=yes
  bl_applicationid='&ADLS_APPLICATION_ID'
  bl_accountname='&ADLS_ACCOUNT_NAME'
  bl_filesystem='&ADLS_FILESYSTEM'
  url='jdbc:spark://&DBR_HOST:443/default;
       transportMode=http;ssl=1;
       HTTPPath=&CLUSTER_PATH;
       AuthMech=3;defaultStringColumnLength=255;
       useNativeQuery=1;'
  user=token
  password=&DBR_TOKEN; 


proc sql;
DROP TABLE dbx_bl.spark_cars;
quit;

data dbx_bl.spark_cars;
set sashelp.cars(obs=5);
run;

proc sql;
select * from dbx_bl.spark_cars;
quit;
