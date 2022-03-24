from sqlmodel import select, Session
from app.app.turn.models import PartnerModel, PartnerWorkerModelReadOnly, PartnerWorkerModel, PartnerModelReadOnly


class TestPartnerWorkerModel:
    def test_get_all_pws(self, turn_session: Session):
        statement = select(PartnerWorkerModelReadOnly).limit(100)
        pws = turn_session.exec(statement).all()
        assert pws
        assert len(pws) == 100

    def test_save_pw(self, session: Session):
        pw = PartnerWorkerModel()
        pw.partner_id=39,
        pw.is_ssn_deceased=-1,
        pw.is_ssn_random=-1,
        pw.is_ssn_valid=-1,
        pw.save(session)

    def test_get_pws_and_write(self, turn_session: Session, session: Session):
        statement = select(PartnerWorkerModelReadOnly).limit(5)
        pws = turn_session.exec(statement).all()
        assert pws
        assert len(pws) == 5

        write_pws = [PartnerWorkerModel.load_from_read_only_model(pw) for pw in pws]
        for pw in write_pws:
            session.add(pw)

        session.commit()

class TestPartnerModel:
    def test_get_all_partners(self, turn_session: Session):
        statement = select(PartnerModelReadOnly).limit(100)
        partners = turn_session.exec(statement).all()
        assert partners
        assert len(partners) == 100

    def test_save_partner(self, session: Session):
        PARTNER_NAME = 'PARTNER_NAME'
        PARTNER_ID = 39
        partner = PartnerModel(
            name=PARTNER_NAME,
            id=PARTNER_ID
        )
        partner.save(session)
        