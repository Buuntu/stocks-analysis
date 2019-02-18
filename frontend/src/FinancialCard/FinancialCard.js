import React from 'react';
import {Card} from 'react-bootstrap';
import './FinancialCard.css';

const financial_card = props => {
  return (
    <Card className="FinancialCard">
      <Card.Body>
        <Card.Title>{props.report.reportDate}</Card.Title>
        <button type="button" className="close" aria-label="Close" onClick={props.close}>
          <span aria-hidden="true">&times;</span>
        </button>
      </Card.Body>
    </Card>
  );
}

export default financial_card;
