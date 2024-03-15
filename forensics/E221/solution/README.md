# E221: 

## Write-up

SOC teams do such tests from times to times to assess their detection and response capabilities using RTA. ([Example: Elastic RTA](https://github.com/elastic/detection-rules/tree/main/rta)).
- We're in front of millions of logs collected using the Elastic agent. Ingested and presented in the [ECS](https://www.elastic.co/guide/en/ecs/current/index.html) format.
- In the Discover section, we can filter the documents using:
  - Timestamp: `from Mar 1, 2024 @ 16:53:15.210` to `Mar 1, 2024 @ 17:00:27.841`
  - Query: `user.name: "liz-keen"`
  - Add columns that can help us understand the scenario. `process.command_line` is enough to just get the flag :') meanwhile there were various Mitre Techniques (such as [T1070.002](https://attack.mitre.org/techniques/T1070/002/) by executing `rm -rf /var/log/messages`). I had to inject the flag in just 3 techniques to not make it very annoying.
  
    - Flag part 01: `/home/liz-keen/.../sh -c echo “bmV4dXN7b2hfNG5BTHkkdF8””`
    - Flag part 02: `nslookup 74494d336c314e655f71754552595f.reddington`
    - Flag part 03: `crontab .aW52M3NUSUc0dDNfUjNQMHJ0fQ`
  
This was a very simple challenge, if you found it interesting you may like [OhMyMalware](https://ohmymalware.com/)

## Flag

`nexus{oh_4nALy$t_tIM3l1Ne_quERY_inv3sTIG4t3_R3P0rt}`