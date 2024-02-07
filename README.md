# Docker Example

In this example, we show how you can use [Docker with CodeSandbox](https://codesandbox.io/post/introducing-docker-support-in-codesandbox). Check [the Dockerfile](./.devcontainer/Dockerfile) to see how we configure the container of this sandbox. You can simply edit it yourself and the container will rebuild. Make sure to fork the sandbox first by clicking "Fork" in the top left corner.

- Every new terminal will run inside this new container, open a new terminal with CTRL ~
- We set up an example sandbox task that runs `whereis htop`. Typically this would be where you run `yarn run serve`. You can edit it in [tasks.json](./.codesandbox/tasks.json)

run this command on codesandbox to access db
```
docker exec -it  docker-learn-postgres_devcontainer-db-1 psql -U postgres -d postgres
```

Pour lancer une requette sql dans postegres on utilise la commande
```
psql -U <utilisateur> -d <base_de_donnees> -f <chemin_vers_fichier>
```

```
psql -U postgres -d postgres -f requete.sql
```