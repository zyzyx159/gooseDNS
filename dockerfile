FROM internetsystemsconsortium/bind9
WORKDIR /etc/bind
COPY Bind9/config/named.conf named.conf
COPY ToDo.adoc ToDo.adoc
