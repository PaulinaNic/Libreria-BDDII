class  FacturaLibro :
    factura_id : int
    isbn : chr
    cantidadLibro : int
    def  __init__ ( self , factura_id : int, isbn : chr, cantidadLibro : int ) ->  None :
        self.factura_id = factura_id
        self.isbn = isbn
        self.cantidadLibro = cantidadLibro