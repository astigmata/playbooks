# playbooks repository

Tested on microk8s 1.24  
Required: Traefik, cert-manager

## [kubernetes_jenkins](kubernetes_jenkins.yml)
Playbook to deploy Jenkins on a kubernetes cluster from Helm package.  

## [kubernetes_excalidraw](kubernetes_excalidraw.yml)
Playbook to deploy the greatest tool Excalidraw on kubernetes

## [kubernetes_pgadmin](kubernetes_pgadmin.yml)
Playbook to deploy pgadmin4 on a kubernetes cluster from Helm package.

## [kubernetes_harbor](kubernetes_harbor.yml)
Playbook to deploy Harbor on a kubernetes cluster from Helm package.

## [kubernetes_qbittorrent](kubernetes_qbittorrent.yml)
Playbook to deploy qbittorrent on kubernetes.

## [kubernetes_bitbucket_server](kubernetes_bitbucket_server.yml)
Playbook to deploy BitBucket Server Atlassian from Helm package.

## [kubernetes_kubegres_operator](kubernetes_kubegres_operator.yml)
Playbook to deploy Kubegres Operator from Helm package.

## [kubernetes_kubegres_database](kubernetes_kubegres_database.yml)
Playbook to deploy Postgres database with Kubegres Operator.

## [kubernetes_awx_operator](kubernetes_awx_operator.yml)
Playbook to deploy AWX from awx-operator on Kubernetes.

### To deploy AWX with an external postgres database  

Deploy [kubernetes_kubegres_operator](kubernetes_kubegres_operator.yml)

Deploy [kubernetes_kubegres_database](kubernetes_kubegres_database.yml) with:
```yaml
postgres_superuser_pwd: myPostgresAdminPassword
postgres_replica_pwd: myReplicaPassword
postgres_database_size: 8Gi
postgres_version: 13
postgres_database_name: awx
postgres_pwd: myPostgresPassword
postgres_username: awx
```

Deploy [kubernetes_awx_operator](kubernetes_awx_operator.yml) with:
```yaml
awx_postgres_username: awx
awx_postgres_pwd: myPostgresPassword
awx_postgres_database: awx
awx_external_database: true
```

### To deploy AWX without any external database

Deploy [kubernetes_awx_operator](kubernetes_awx_operator.yml) with:
```yaml
awx_postgres_username: awx
awx_postgres_pwd: myPostgresPassword
awx_postgres_database: awx
```