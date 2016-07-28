import sys
import json
import re
from boto.ec2 import EC2Connection


def get_security_group_rules_as_dict(rules):
    security_group_rules = []
    for rule in rules:
        rule_dict = {'proto': str(rule.ip_protocol), 'from_port': rule.from_port, 'to_port': rule.to_port}
        for grant in rule.grants:
            rule_dict_with_source = rule_dict
            if re.search("sg-", str(grant)):
                rule_dict_with_source['group_name'] = str(grant)
            else:
                rule_dict_with_source['cidr_ip'] = str(grant)
            security_group_rules.append(rule_dict_with_source)
    return security_group_rules

ec2_connection = EC2Connection()
group_id = sys.argv[1]
security_group = ec2_connection.get_all_security_groups(group_ids=[group_id])

security_group_details = dict()
security_group_details["id"] = security_group[0].id
security_group_details["tag"] = security_group[0].tags
security_group_details["name"] = security_group[0].name
security_group_details["description"] = security_group[0].description
security_group_details["vpc_id"] = security_group[0].vpc_id
security_group_details["rules"] = get_security_group_rules_as_dict(security_group[0].rules)
security_group_details["rules_egress"] = get_security_group_rules_as_dict(security_group[0].rules_egress)

print json.dumps(security_group_details)

