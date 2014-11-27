import os
from flask import Flask, render_template
import pandas as p
import json
from collections import defaultdict

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/test_scatter')
def test_scatter():
    return render_template('test_scatter.html')

@app.route('/api/v1/test_e4_full')
def test_e4_full_data():
    t = p.read_table("data/TestE4_full_with_species.csv", 
                 header=0, index_col=0, sep=',')
    genomes = defaultdict(list)
    for contig,row in t.iterrows():
        genomes[row['Genome']].append({'contig': contig, 'x': row['0'], 'y': row['1']})
    return json.dumps(genomes)

@app.route('/api/v1/test_e4_one')
def test_e4_one_data():
    t = p.read_table("data/TestE4_one_sample_with_species.csv", 
                 header=0, index_col=0, sep=',')
    genomes = defaultdict(list)
    for contig,row in t.iterrows():
        genomes[row['Genome']].append({'contig': contig, 'x': row['0'], 'y': row['1']})
    return json.dumps(genomes)

@app.route('/test_e4_one')
def test_e4_one():
    return render_template('scatter.html',data_url='/api/v1/test_e4_one')

@app.route('/test_e4_full')
def test_e4_full():
    return render_template('scatter.html',data_url='/api/v1/test_e4_full')


if __name__ == '__main__':
    app.run(debug=True)
