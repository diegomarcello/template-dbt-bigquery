import datetime

import codecs
import csv

import apache_beam as beam

from apache_beam.io.gcp.bigquery_file_loads import BigQueryBatchFileLoads
from apache_beam.options.pipeline_options import StandardOptions, PipelineOptions
from typing import Dict, Iterable, List


BQ_TABLE = "despesas_cota_exercicio_atividade_parlamentar"
BQ_DATASET = "raw_zone"
BQ_PROJECT = "edw-corp-bigquery-20211228-dev"

HEAD=["txNomeParlamentar","cpf","ideCadastro","nuCarteiraParlamentar","nuLegislatura","sgUF","sgPartido","codLegislatura","numSubCota","txtDescricao","numEspecificacaoSubCota","txtDescricaoEspecificacao","txtFornecedor","txtCNPJCPF","txtNumero","indTipoDocumento","datEmissao","vlrDocumento","vlrGlosa","vlrLiquido","numMes","numAno","numParcela","txtPassageiro","txtTrecho","numLote","numRessarcimento","vlrRestituicao","nuDeputadoId","ideDocumento","urlDocumento"]

def prepare(element):

    line = element.split(";")
    vals = []
    for item in line:
        vals.append(item.replace('"', ''))

    element_ret = dict(zip(HEAD, vals))

    return element_ret

def run():

    input_files='data/*.csv'

    pipeline_options = PipelineOptions()

    pipeline_options.view_as(StandardOptions).runner = "DirectRunner"
    p = beam.Pipeline(options=pipeline_options)
    

    (p | "Read from csv" >> beam.io.ReadFromText(input_files)
    | 'convert entity' >> beam.Map(prepare)
    | 'write append' >> BigQueryBatchFileLoads(
            destination=f"{BQ_PROJECT}:{BQ_DATASET}.{BQ_TABLE}",
            custom_gcs_temp_location=f'gs://gcs-3d23620d33571f6fbbe3f1d46e07652b/append',
            write_disposition='WRITE_APPEND',
            create_disposition='CREATE_IF_NEEDED',
            schema='SCHEMA_AUTODETECT')
    )
    p.run().wait_until_finish()


if __name__ == "__main__":
    # create_datastore_entity()
    run()