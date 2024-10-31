# ETFS.py

# Definición de la lista de instrumentos financieros
instrumentos_financieros = [
    {
        "nombre": "AZ China",
        "descripcion": "Replica el índice MSCI China, proporcionando exposición a empresas de gran y mediana capitalización en China. Ideal para quienes buscan diversificación en sectores clave de la economía china, como tecnología y consumo.",
        "simbolo": "MCHI",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI TAIWAN INDEX FD",
        "descripcion": "Sigue el índice MSCI Taiwan, dando acceso a empresas taiwanesas importantes, especialmente en tecnología. Es popular entre inversores interesados en el sector de semiconductores y fabricación en Asia.",
        "simbolo": "EWT",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ RUSSELL 2000",
        "descripcion": "Representa el índice Russell 2000 de empresas de pequeña capitalización en EE. UU., ofreciendo exposición al crecimiento del mercado interno estadounidense. Es ideal para inversores buscando diversificación en empresas emergentes.",
        "simbolo": "IWM",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ Brasil",
        "descripcion": "Sigue el índice MSCI Brazil, brindando exposición a empresas brasileñas en sectores como energía y finanzas. Permite a los inversionistas acceder al mercado emergente de Brasil y su potencial de crecimiento.",
        "simbolo": "EWZ",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI UNITED KINGDOM",
        "descripcion": "Este ETF replica el índice MSCI United Kingdom, ofreciendo exposición a grandes empresas británicas. Ideal para quienes buscan diversificación en sectores británicos de finanzas, salud y energía.",
        "simbolo": "EWU",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ DJ US FINANCIAL SECT",
        "descripcion": "Sigue el índice MSCI BRIC, exponiendo a los mercados emergentes de Brasil, Rusia, India y China. Es ideal para diversificación geográfica en los países BRIC con alto potencial de crecimiento.",
        "simbolo": "IYF",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ BRIC",
        "descripcion": "Sigue el índice MSCI BRIC, exponiendo a los mercados emergentes de Brasil, Rusia, India y China. Es ideal para diversificación geográfica en los países BRIC con alto potencial de crecimiento.",
        "simbolo": "BKF",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI SOUTH KOREA IND",
        "descripcion": "Representa el índice MSCI South Korea, con exposición a grandes empresas surcoreanas como Samsung. Este ETF es ideal para inversores interesados en tecnología y consumo en Corea del Sur.",
        "simbolo": "EWY",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ BARCLAYS AGGREGATE",
        "descripcion": "Sigue el índice Barclays U.S. Aggregate Bond, ofreciendo acceso a bonos del gobierno y corporativos en EE. UU. Es una opción de baja volatilidad para ingresos estables.",
        "simbolo": "AGG",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ Mercados Emergentes",
        "descripcion": "Replica el índice MSCI Emerging Markets, proporcionando acceso a mercados emergentes de Asia, América Latina y más. Ideal para inversores buscando exposición en economías en desarrollo.",
        "simbolo": "EEM",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI EMU",
        "descripcion": "Este ETF sigue el índice MSCI Eurozone, ofreciendo acceso a empresas en la zona euro. Ideal para quienes buscan diversificación en empresas europeas de gran y mediana capitalización.",
        "simbolo": "EZU",
        "moneda": "EUR",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ FTSE/XINHUA CHINA 25",
        "descripcion": "ETF que sigue el índice FTSE/Xinhua China 25, centrado en grandes empresas chinas. Proporciona exposición a sectores clave como bancos, telecomunicaciones y energía en China.",
        "simbolo": "FXI",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ Oro",
        "descripcion": "ETF que sigue el precio del oro, ofreciendo exposición directa a este metal precioso sin necesidad de poseer el activo físico. Es ideal para quienes buscan una cobertura contra la inflación.",
        "simbolo": "GLD",
        "moneda": "USD",
        "paga_dividendos": "No"
    },
    {
        "nombre": "AZ LATIXX MEX CETETRAC",
        "descripcion": "Índice mexicano de CETES, permitiendo acceso a bonos emitidos por el gobierno mexicano. Ofrece una inversión de bajo riesgo con rendimientos en moneda nacional.",
        "simbolo": "CETETRC.MX",
        "moneda": "MXN",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ QQQ NASDAQ 100",
        "descripcion": "Sigue el índice Nasdaq 100, que incluye las 100 principales empresas tecnológicas no financieras de EE. UU. Es ideal para inversionistas interesados en tecnología e innovación.",
        "simbolo": "QQQ",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI ASIA EX-JAPAN",
        "descripcion": "Este ETF ofrece exposición a acciones de Asia sin incluir Japón. Es ideal para quienes buscan diversificación en mercados asiáticos emergentes y desarrollados.",
        "simbolo": "AAXJ",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ LATIXX MEX M10TRAC",
        "descripcion": "Fondo basado en bonos M10 en México, invirtiendo en deuda gubernamental a mediano plazo. Es ideal para quienes buscan estabilidad en moneda local con menor volatilidad.",
        "simbolo": "M10TRAC.MX",
        "moneda": "MXN",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ BARCLAYS 1-3 YEAR TR",
        "descripcion": "Sigue el índice Barclays 1-3 Year Treasury, ofreciendo bonos a corto plazo del Tesoro de EE. UU. Ideal para inversores que buscan estabilidad y baja duración en renta fija.",
        "simbolo": "SHY",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI ACWI INDEX FUND",
        "descripcion": "ETF que sigue el índice MSCI All Country World Index, brindando exposición a mercados globales. Es ideal para diversificación en acciones de distintos países y sectores.",
        "simbolo": "ACWI",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ LATIXX MEXICO M5TRAC",
        "descripcion": "Fondo de bonos M5 en México, enfocado en deuda gubernamental a largo plazo. Ofrece una opción de inversión en pesos mexicanos con rendimientos estables.",
        "simbolo": "M5TRAC.MX",
        "moneda": "MXN",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ SILVER TRUST",
        "descripcion": "ETF que sigue el precio de la plata, proporcionando exposición al metal sin necesidad de poseerlo físicamente. Es una opción para diversificación en metales preciosos.",
        "simbolo": "SLV",
        "moneda": "USD",
        "paga_dividendos": "No"
    },
    {
        "nombre": "AZ MSCI HONG KONG INDEX",
        "descripcion": "Sigue el índice MSCI Hong Kong, ofreciendo acceso a empresas importantes en Hong Kong. Ideal para quienes buscan exposición en el mercado asiático en sectores como finanzas y propiedades.",
        "simbolo": "EWH",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ LATIXX MEX UDITRAC",
        "descripcion": "Fondo mexicano relacionado con UDIS, una unidad de inversión ajustada por inflación en México. Ofrece protección contra la inflación con rendimientos en moneda local.",
        "simbolo": "UDITRAC.MX",
        "moneda": "MXN",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ SPDR S&P 500 ETF TRUST",
        "descripcion": "ETF que sigue el índice S&P 500, incluyendo las 500 principales acciones de EE. UU. Es uno de los ETFs más populares para diversificación en el mercado estadounidense.",
        "simbolo": "SPY",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI JAPAN INDEX FD",
        "descripcion": "Sigue el índice MSCI Japan, proporcionando acceso a grandes empresas japonesas. Ideal para quienes buscan exposición en el mercado japonés de manera diversificada.",
        "simbolo": "EWJ",
        "moneda": "JPY",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ BG EUR GOVT BOND 1-3",
        "descripcion": "ETF centrado en bonos gubernamentales europeos a corto plazo. Es una inversión de baja volatilidad para quienes buscan ingresos estables en euros.",
        "simbolo": "IBGS.AS",
        "moneda": "EUR",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ SPDR DJIA TRUST",
        "descripcion": "ETF que sigue el índice Dow Jones Industrial Average, representando 30 de las principales empresas de EE. UU. Ideal para exposición a sectores clave de la economía estadounidense.",
        "simbolo": "DIA",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI FRANCE INDEX FD",
        "descripcion": "Sigue el índice MSCI France, ofreciendo exposición a empresas líderes francesas. Es ideal para diversificación en el mercado francés en sectores como finanzas y consumo.",
        "simbolo": "EWQ",
        "moneda": "EUR",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ DJ US OIL & GAS EXPL",
        "descripcion": "Fondo enfocado en el sector de exploración de petróleo y gas en EE. UU., invirtiendo en empresas del sector energético. Es ideal para quienes buscan exposición en el mercado de energía estadounidense.",
        "simbolo": "IEO",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ VANGUARD EMERGING MARKET ETF",
        "descripcion": "Sigue mercados emergentes, con exposición a empresas en Asia, América Latina, y más. Atrae a inversores interesados en el crecimiento de economías en desarrollo.",
        "simbolo": "VWO",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI AUSTRALIA INDEX",
        "descripcion": "ETF que sigue el índice MSCI Australia, invirtiendo en empresas australianas de gran y mediana capitalización. Proporciona diversificación en sectores clave de la economía australiana.",
        "simbolo": "EWA",
        "moneda": "AUD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ IPC LARGE CAP TR TRAC",
        "descripcion": "Índice de capitalización grande del mercado mexicano, con las principales acciones de la Bolsa Mexicana de Valores. Proporciona exposición diversificada al mercado mexicano.",
        "simbolo": "ILCTRAC.MX",
        "moneda": "MXN",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ FINANCIAL SELECT SECTOR SPDR",
        "descripcion": "ETF enfocado en el sector financiero de EE. UU., incluyendo bancos y aseguradoras. Ideal para quienes buscan invertir en el crecimiento del sector financiero.",
        "simbolo": "XLF",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI CANADA",
        "descripcion": "Este ETF sigue el índice MSCI Canada, proporcionando acceso a empresas importantes en Canadá. Es ideal para diversificación en sectores como energía y finanzas canadienses.",
        "simbolo": "EWC",
        "moneda": "CAD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ S&P LATIN AMERICA 40",
        "descripcion": "Sigue el índice S&P Latin America 40, invirtiendo en empresas líderes de América Latina. Es ideal para diversificación en el crecimiento de economías latinoamericanas.",
        "simbolo": "ILF",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ HEALTH CARE SELECT SECTOR",
        "descripcion": "ETF centrado en el sector salud de EE. UU., incluyendo farmacéuticas y biotecnología. Ideal para exposición en uno de los sectores más estables y crecientes.",
        "simbolo": "XLV",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ MSCI GERMANY INDEX",
        "descripcion": "Sigue el índice MSCI Germany, ofreciendo acceso a empresas alemanas de gran y mediana capitalización. Es ideal para diversificación en el mercado alemán en sectores como industria y finanzas.",
        "simbolo": "EWG",
        "moneda": "EUR",
        "paga_dividendos": "Sí"
    },
    {
        "nombre": "AZ INDUSTRIAL SELECT SECTOR SPDR",
        "descripcion": "ETF que sigue el sector industrial de EE. UU., con exposición a empresas de manufactura, transporte, y más. Es adecuado para quienes buscan diversificación en el sector industrial estadounidense.",
        "simbolo": "XLI",
        "moneda": "USD",
        "paga_dividendos": "Sí"
    }
]

# ETFS.py

def obtener_informacion_etf(simbolo):
    """
    Busca y retorna la información de un ETF específico por su símbolo.
    
    Parámetros:
    - simbolo (str): El símbolo del ETF a buscar.
    
    Retorna:
    - dict: Un diccionario con la información del ETF encontrado o None si no existe.
    """
    for etf in instrumentos_financieros:
        if etf["simbolo"] == simbolo:
            return etf
    return None

