# -*- coding: utf-8 -*-

from odoo import models, fields, api

class libreria_categoria( models.Model ):
    _name = "libreria.categoria"#campo privado similar al codigo del objeto
    name = fields.Char( string = "Nombre", required = True, help = "Introduce el nombre" )
    descripcion = fields.Text( string = "Descripcion" )
    #un libro solo pertenece a una categoria
    libros = fields.One2many( 'libreria.libro', 'categoria', string = 'Libros' )

class libreria_libro( models.Model ):
    _name = "libreria.libro"
    name = fields.Char( string = "Título", required = True )
    precio = fields.Float( string = "Precio" )
    ejemplares = fields.Integer( string = "Ejemplares" )
    segundamano = fields.Boolean( string = 'Segunda Mano' )
    fecha = fields.Date( string = 'Fecha de compra' )
    estado = fields.Selection( [ ("0", 'Bueno'), ('1', 'Regular'), ('2', 'Malo') ], string = "Estado", default = "0" )
    #a una categoria pertenece muchos libros
    categoria = fields.Many2one( 'libreria.categoria', string = 'Categoria', required = True, ondelete = 'cascade' )
    #añadir campo calculado :D
    #store true se almacena en la base de datos
    importetotal = fields.Float( string = 'Importe total', compute = '_importetotal', store = True )
    @api.depends( 'precio', 'ejemplares' )

    #declaracion de un procedimiento
    #siempre lleva dos puntos al final de la declaración de una clase, procedimiento, while, for :o
    def _importetotal( self ):
        for r in self:
            r.importetotal = r.ejemplares*r.precio
