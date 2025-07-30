---
id: setup
title: Preparar tu clúster Raspberry Pi
sidebar_position: 2
---

# Preparar tu clúster Raspberry Pi

En esta guía instalaremos el sistema operativo, configuraremos la red y dejaremos listo el clúster para ejecutar trabajos distribuidos.

## 1. Grabar Raspberry Pi OS en la SD

1. Descarga **Raspberry Pi OS (64‑bit)** desde la página oficial.
2. Utiliza una herramienta como **Balena Etcher** para grabar la imagen en tu tarjeta SD.
3. Crea un archivo vacío llamado `ssh` en la partición `boot` para habilitar el acceso remoto.

## 2. Primer arranque y configuración básica

1. Inserta la SD en la Pi y conéctala a la red.
2. Accede por SSH con `ssh pi@<ip>` (contraseña por defecto: `raspberry`).
3. Ejecuta `sudo raspi-config` para definir el idioma, zona horaria y usuario.
4. Actualiza el sistema: `sudo apt update && sudo apt upgrade -y`.

## 3. Configurar IP estática y claves SSH

1. Edita `/etc/dhcpcd.conf` para asignar una IP fija a cada nodo.
2. Genera un par de claves: `ssh-keygen -t rsa -b 4096` y copia la clave pública a los nodos con `ssh-copy-id`.
3. Usa `nmap` o `arp-scan` para descubrir dispositivos en tu red y verificar conectividad.

## 4. Montar almacenamiento compartido (NFS)

1. En el nodo maestro instala el servidor: `sudo apt install nfs-kernel-server`.
2. Crea un directorio a exportar, por ejemplo `/export/home`, y añade una entrada en `/etc/exports`:

   ```
   /export/home *(rw,sync,no_root_squash)
   ```

3. En cada nodo instala el cliente NFS: `sudo apt install nfs-common` y monta la carpeta:

   ```bash
   sudo mount master:/export/home /home/shared
   ```

4. Añade la entrada correspondiente a `/etc/fstab` para montar automáticamente al iniciar.

## 5. Instalar y configurar SLURM

1. En el maestro instala `slurmctld` y en los nodos `slurmd`.
2. Copia un archivo `slurm.conf` adecuado (ver ejemplos en los slides) y define una partición llamada `rpi` con los nodos disponibles.
3. Inicia los servicios (`systemctl start slurmctld` y `slurmd`) y usa `sinfo` para verificar el estado.

Una vez completados estos pasos, ¡tu clúster estará listo para ejecutar tareas paralelas!
