#!/usr/bin/env python3
from download_github_tree import download_github_tree

########################################## Downloading roles folders...
download_github_tree(
    "https://github.com/geerlingguy/ansible-role-swap/tree/master", "geerlingguy.swap"
)
download_github_tree(
    "https://github.com/robertdebock/ansible-role-logrotate/tree/master",
    "robertdebock.logrotate",
)
download_github_tree(
    "https://github.com/Oefenweb/ansible-fail2ban/tree/master", "oefenweb.fail2ban"
)
download_github_tree(
    "https://github.com/hifis-net/ansible-collection-toolkit/tree/main/roles/unattended_upgrades",
    "hifis.unattended_upgrades",
)
download_github_tree(
    "https://github.com/patrickjahns/ansible-role-promtail/tree/master",
    "patrickjahns.promtail",
)
download_github_tree(
    "https://github.com/dmotte/ansible-role-podman/tree/main", "dmotte.podman"
)
download_github_tree(
    "https://github.com/geerlingguy/ansible-role-docker/tree/master",
    "geerlingguy.docker",
)
download_github_tree(
    "https://github.com/sdarwin/Ansible-VNC/tree/master", "sdarwin.VNC"
)
download_github_tree(
    "https://github.com/gikeymarcia/ansible-role-neovim/tree/master",
    "gikeymarcia.neovim",
)
