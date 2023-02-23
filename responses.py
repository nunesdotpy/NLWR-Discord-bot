def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '$ajuda':
        return 'Comandos:\n`$ips` Lista com os IPs dos nossos servidores.\n`$ajuda` Lista de comandos\n`p$[comando]` Responde o comando solicitado no chat privado'

    if p_message == '$ips':
        return '```CSS\n[Servidores da North Lion Warriors]```\nTS3```ts3.nlwr.net```\nCS MIX```connect 35.247.192.35:27015;password nlwr```\n> https://gaming.nlwr.net/'