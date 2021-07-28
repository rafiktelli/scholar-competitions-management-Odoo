# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
class Competition(models.Model):
    _name = 'esicompet.competition'
    _description = "EsiCompet Competitions"

    name = fields.Char(string="Titre/Nom", required=True)
    validated = fields.Boolean('Validée', default=False)
    description = fields.Text(string="description")
    place = fields.Char(string="Lieu")
    start_date = fields.Date(string="Date début")
    end_date = fields.Date(string="Date fin")
    seats = fields.Integer(string="Nombre de places")
    
    participation_ids = fields.One2many(
        'esicompet.participation', 'competition_id', string="Participations")


class Paticipation(models.Model):
    _name = 'esicompet.participation'
    _description = "EsiCompet Participations"

    name = fields.Char(required=True)
    grade = fields.Selection([('1CP', '1ére Année en Classes Préparatoires'),('2CP', '2ième Année en Classes Préparatoires'),('1CS', '1ére Année en Classes Supérieures'), ('2CS', '2ième Année en Classes Supérieures'), ('3CS', '3ième Année en Classes Supérieures')], string='Niveau')
    supervisor_name = fields.Char(string="nom organisateur")
    supervisor_type = fields.Selection([('National','National'),('International','International')], string="type organisateur")
    ressources = fields.Binary(string="Estimation des ressources nécessaires")
    
    
    competition_id = fields.Many2one('esicompet.competition',
        ondelete='cascade', string="Competition", required=True)
    
    enseignant_id = fields.Many2one('esicompet.enseignant',
        ondelete='cascade', string="Enseignant encadreur")

    
class Enseignant(models.Model):
    _name = 'esicompet.enseignant'
    _description = 'EsiCompet Enseignants Tuteurs'

    name = fields.Char(String="nom", required=True)
    email = fields.Char(String="email")
    nb_etud = fields.Integer(string="Nombre d'étudiants à suivre")
