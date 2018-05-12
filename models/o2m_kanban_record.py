# -*- coding: utf-8 -*-

from openerp import api, models
import logging
_logger = logging.getLogger(__name__)

class O2mKanbanRecord(models.Model):
    _name = "kanban.record"

    @api.model
    def getKanbanRecord(self, records, o2m_dataset):
        updated_record = []
        ids_list = []
        _logger.info('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        _logger.info('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        _logger.info('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        for record in records:
            _logger.info('xxxxxxxxxxxxxxxxxx        record      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxxxxxxxxxxxxxxx        record      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxxxxxxxxxxxxxxx        record      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxx                            %s                       xxxxxxx',record)
            _logger.info('xxxxxxxxxxxxxxxxxx        o2m_dataset      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxxxxxxxxxxxxxxx        o2m_dataset      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxxxxxxxxxxxxxxx        o2m_dataset      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxx                            %s                       xxxxxxx',o2m_dataset.items())
            for key, value in o2m_dataset.items():
                _logger.info('xxxxxxxxxxxxxxxxxx        key      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxxxxxxxxxxxxxxx        key      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxxxxxxxxxxxxxxx        key      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxx                            %s                       xxxxxxx',key)
                _logger.info('xxxxxxxxxxxxxxxxxx        value      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxxxxxxxxxxxxxxx        value      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxxxxxxxxxxxxxxx        value      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxx                            %s                       xxxxxxx',value)
                ids = record[value["field_name"]]
                _logger.info('xxxxxxxxxxxxxxxxxx        ids      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxxxxxxxxxxxxxxx        ids      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxxxxxxxxxxxxxxx        ids      xxxxxxxxxxxxxxxxxxxxxxxxx')
                _logger.info('xxxxx                            %s                       xxxxxxx',ids)
                # for vals in ids:
                #     ids_list.append(vals)
                res = self.env[value["model"]].browse(tuple(ids))
                _logger.info('1111111111111111111        ids      xxxxxxxxxxxxxxxxxxxxxxxxx')
                res_fields = value["fields"]
                _logger.info('2222222222222222222        ids      xxxxxxxxxxxxxxxxxxxxxxxxx')
                o2m_data = res.search_read([('id', 'in', ids)], res_fields)
                _logger.info('3333333333333333333        ids      xxxxxxxxxxxxxxxxxxxxxxxxx')
                record[value["field_name"]] = o2m_data
                _logger.info('44444444444444444444        ids      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('555555555555555        ids      xxxxxxxxxxxxxxxxxxxxxxxxx')
            updated_record.append(record)
            _logger.info('xxxxxxxxxxxxxxxxxx        updated_record      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxxxxxxxxxxxxxxx        updated_record      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxxxxxxxxxxxxxxx        updated_record      xxxxxxxxxxxxxxxxxxxxxxxxx')
            _logger.info('xxxxx                            %s                       xxxxxxx',updated_record)
        return updated_record
