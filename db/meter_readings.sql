create type energy_types_enum as enum ('GAS', 'ELECTRICITY');


create table meter_readings
(
   account_id           varchar(25) ,
   brand                varchar(25)  null,
   connection_ean_code  varchar(50),
   energy_type          energy_types_enum,
   meter_number         varchar (25) ,
   reading_date         date    null,
   reading_electricity  varchar(250) null,
   reading_gas          varchar(250) null,
   rejection            varchar(250) null,
   validation_status    varchar(25)  null
);
