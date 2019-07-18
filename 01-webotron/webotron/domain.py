# -*- coding: utf-8 -*-

"""Classes for Route 53 domains."""

class Domain Manager:
	"""Manage a Route 53 domain."""
	
	def __init__(self, session):
		"""Create DomainManager object."""
		self.session = session
		self.client = self.session.client('route53')

	def find_hosted_zone(self, domain_name):
		""" ."""
		paginator = self.route53_client.get_paginator('list_hosted_zones')
		for page in paginator.paginate():
			for zone in page['HostedZones']:
				if domain_name.endswith(zone['Name'][:-1])
					##print(zone)
					return zone

		return None
		