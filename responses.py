def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '$ajuda':
        return 'Comandos:\n`$ip` Lista com os IPs dos nossos servidores.\n`$ajuda` Lista de comandos\n`p$[comando]` Responde o comando solicitado no chat privado'

    if p_message == '$ip':
        return '```CSS\n[Servidores da North Lion Warriors]```\nTS3```ts3.nlwr.net```\nCS MIX```connect 34.151.254.204:27015;password gxngaming```\n> https://gaming.nlwr.net/'