#!/usr/bin/sh

echo "Installing Starship"
curl -sS https://starship.rs/install.sh | sh -s -- -y > /dev/null
mkdir -p ~/.config
touch ~/.config/starship.toml
starship preset no-nerd-font -o ~/.config/starship.toml
echo 'eval "$(starship init bash)"' >> ~/.bashrc
echo "Starship installed"